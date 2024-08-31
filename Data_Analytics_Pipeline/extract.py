import pandas as pd

def extract_data(file_path):
    print(f"Attempting to read file: {file_path}")
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    data = extract_data('data/raw_data.csv')
    print(data.head())


