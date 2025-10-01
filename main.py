from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_data

def run_pipeline():
    raw_data = extract_data()
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)

if __name__ == "__main__":
    run_pipeline()

