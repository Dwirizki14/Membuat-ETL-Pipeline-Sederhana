def load_data(df, filename='products.csv'):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
