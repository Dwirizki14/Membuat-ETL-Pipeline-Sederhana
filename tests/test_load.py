import unittest
import os
import pandas as pd
from utils.load import load_data

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })
        self.test_filepath = 'tests/test_output.csv'
        self.default_filepath = 'products.csv'

    def tearDown(self):
        # Bersihin file yang dibuat selama test
        if os.path.exists(self.test_filepath):
            os.remove(self.test_filepath)
        if os.path.exists(self.default_filepath):
            os.remove(self.default_filepath)

    def test_load_data_creates_file_with_custom_name(self):
        load_data(self.df, self.test_filepath)
        self.assertTrue(os.path.exists(self.test_filepath))

    def test_load_data_creates_file_with_default_name(self):
        load_data(self.df)  
        self.assertTrue(os.path.exists(self.default_filepath))

    def test_load_data_content(self):
        load_data(self.df, self.test_filepath)
        df_loaded = pd.read_csv(self.test_filepath)
        pd.testing.assert_frame_equal(df_loaded, self.df)

if __name__ == '__main__':
    unittest.main()
