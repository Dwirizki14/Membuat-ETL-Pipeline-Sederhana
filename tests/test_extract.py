import unittest
from unittest.mock import patch, Mock
import pandas as pd

from utils.extract import extract_data  

class TestExtract(unittest.TestCase):
    @patch('utils.extract.requests.get')
    def test_extract_basic(self, mock_get):
        html_content = '''
        <div class="collection-card">
            <h3 class="product-title">Test Product</h3>
            <div class="price-container">$10.00</div>
            <div class="product-details">
                <p style="color:red;">Rating: ⭐ 4.5 / 5</p>
                <p style="color:red;">3 Colors</p>
                <p style="color:red;">Size: M</p>
                <p style="color:red;">Gender: Male</p>
            </div>
        </div>
        '''
        # Buat mock response yang punya atribut status_code dan text
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = html_content
        mock_get.return_value = mock_response

        df = extract_data(max_pages=1)

        self.assertEqual(len(df), 1)
        self.assertIn('title', df.columns)
        self.assertEqual(df.iloc[0]['title'], 'Test Product')
        self.assertEqual(df.iloc[0]['price_raw'], '$10.00')
        self.assertAlmostEqual(df.iloc[0]['rating'], 4.5)

if __name__ == '__main__':
    unittest.main()
