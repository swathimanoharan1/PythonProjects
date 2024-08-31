import pandas as pd

def analyze_data(data):
    summary = data.describe()
    return summary

if __name__ == "__main__":
    data = pd.read_csv('data/transformed_data.csv')
    analysis = analyze_data(data)
    print(analysis)