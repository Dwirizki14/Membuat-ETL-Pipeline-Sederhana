import unittest
import pandas as pd
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def setUp(self):
        # contoh data mentah untuk uji transformasi
        self.raw_data = pd.DataFrame({
            'title': ['Product A', 'Product B'],
            'price_raw': ['$100', '$200'],
            'rating': ['4.5 / 5', 'Invalid Rating'],
            'colors': ['3 Colors', '2 Colors'],
            'size': ['Size: M', 'Size: L'],
            'gender': ['Gender: Male', 'Gender: Female']
        })

    def test_transform_basic(self):
        transformed = transform_data(self.raw_data)

        # cek kolom price sudah float64 dan tidak ada nilai null
        self.assertEqual(transformed['price'].dtype, 'float64')
        self.assertTrue(all(transformed['price'].notnull()))
        self.assertTrue(all(transformed['price'] >= 0))

        # cek kolom rating sudah float dan tidak ada string invalid
        self.assertEqual(transformed['rating'].dtype, 'float64')
        self.assertTrue(all((transformed['rating'] >= 0) & (transformed['rating'] <= 5)))

        # cek kolom colors berisi angka (integer)
        self.assertTrue(all(transformed['colors'].apply(lambda x: isinstance(x, int))))

        # cek kolom size bertipe string tanpa 'Size: '
        self.assertTrue(all(transformed['size'].apply(lambda x: isinstance(x, str))))
        self.assertFalse(any(transformed['size'].str.contains('Size:')))

        # cek kolom gender bertipe string tanpa 'Gender: '
        self.assertTrue(all(transformed['gender'].apply(lambda x: isinstance(x, str))))
        self.assertFalse(any(transformed['gender'].str.contains('Gender:')))

if __name__ == '__main__':
    unittest.main()
