# Membuat-ETL-Pipeline-Sederhana

##  Cara Menjalankan Script ETL Pipeline

1. Pastikan semua dependencies telah diinstall:
   pip install -r requirements.txt

2. Jalankan script ETL end-to-end:
   python main_etl.py

   Script ini akan melakukan:
   - Extract data dari situs fashion-studio.dicoding.dev
   - Transform data sesuai ketentuan
   - Load data ke file CSV 
---

##  Cara Menjalankan Unit Test

1. Pastikan berada di direktori proyek, lalu jalankan:
   python -m unittest discover -s tests

   Ini akan menjalankan semua pengujian di folder `tests/` secara otomatis.

---

## Cara Menjalankan Test Coverage

1. Install terlebih dahulu:
   pip install coverage

2. Jalankan perintah untuk mengukur cakupan pengujian:
   coverage run -m unittest discover -s tests

3. Lihat hasil test coverage-nya:
   coverage report -m

