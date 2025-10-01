import pandas as pd
import numpy as np
import re

def transform_data(df):
    # Fungsi parsing harga USD ke float Rupiah
    def parse_price(price_str):
        if pd.isna(price_str) or price_str.strip() == '':
            return np.nan
        if "Price Unavailable" in price_str:
            return np.nan
        try:
            price_usd = float(price_str.replace('$', '').replace(',', '').strip())
            price_rp = price_usd * 16000
            return float(price_rp)
        except:
            return np.nan

    # Buat kolom price baru hasil konversi
    df['price'] = df['price_raw'].apply(parse_price).astype('float64')

    # Hapus kolom price_raw karena tidak diperlukan
    df = df.drop(columns=['price_raw'])

    # Pindahkan kolom price tepat setelah kolom title
    cols = df.columns.tolist()
    cols.remove('price')
    idx_title = cols.index('title') + 1
    cols.insert(idx_title, 'price')
    df = df[cols]

    # Parse rating jadi float, invalid jadi NaN
    def parse_rating(r):
        try:
            if isinstance(r, str):
                r = r.split('/')[0].strip()
            rating_float = float(r)
            return rating_float
        except:
            return np.nan
    df['rating'] = df['rating'].apply(parse_rating).astype('float64')

    # Ambil angka dari colors (contoh: "3 Colors" -> 3)
    def extract_colors_number(s):
        if isinstance(s, str):
            match = re.search(r'\d+', s)
            if match:
                return int(match.group())
        return np.nan
    df['colors'] = df['colors'].apply(extract_colors_number).astype('Int64')  # nullable int

    # Bersihkan Size dari "Size: "
    df['size'] = df['size'].apply(lambda s: s.replace('Size: ', '').strip() if isinstance(s, str) else s).astype('string')

    # Bersihkan Gender dari "Gender: "
    df['gender'] = df['gender'].apply(lambda s: s.replace('Gender: ', '').strip() if isinstance(s, str) else s).astype('string')

    # Hapus baris duplikat, null, dan invalid title
    df = df.drop_duplicates()
    df = df.dropna()
    df = df[df['title'] != 'Unknown Product']

    return df