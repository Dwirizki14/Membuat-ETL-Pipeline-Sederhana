import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_data(max_pages=50):
    all_products = []
    scrape_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for page in range(1, max_pages + 1):
        url = 'https://fashion-studio.dicoding.dev/' if page == 1 else f'https://fashion-studio.dicoding.dev/page{page}'
        print(f"Extracting page {page} from {url}...")

        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to get page {page}, status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='collection-card')
        if not products:
            print("No products found, stopping extraction.")
            break

        for prod in products:
            title_tag = prod.find('h3', class_='product-title')
            price_tag = prod.find('div', class_='price-container')
            if not price_tag:
                price_tag = prod.find('span', class_='price')

            price_raw = price_tag.get_text(strip=True) if price_tag else ''

            details_div = prod.find('div', class_='product-details')
            rating = 0.0
            colors = ''
            size = ''
            gender = ''

            if details_div:
                p_tags = details_div.find_all('p', style=True)
                if len(p_tags) >= 4:
                    rating_text = p_tags[0].get_text(strip=True)
                    try:
                        rating_str = rating_text.split('Rating:')[-1].split('/')[0].replace('⭐', '').strip()
                        rating = float(rating_str)
                    except:
                        rating = 0.0
                    colors = p_tags[1].get_text(strip=True)
                    size = p_tags[2].get_text(strip=True)
                    gender = p_tags[3].get_text(strip=True)

            title = title_tag.get_text(strip=True) if title_tag else 'Unknown Product'

            all_products.append({
                'title': title,
                'price_raw': price_raw,
                'rating': rating,
                'colors': colors,
                'size': size,
                'gender': gender,
                'timestamp': scrape_time
            })

    df = pd.DataFrame(all_products)
    return df
