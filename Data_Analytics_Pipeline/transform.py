def transform_data(data):
    data = data[data['Quantity'] > 5]
    return data

if __name__ == "__main__":
    from extract import extract_data
    raw_data = extract_data("data/raw_data.csv")
    transformed_data = transform_data(raw_data)
    transformed_data.to_csv('data/transformed_data.csv', index=False)
    print(type(transformed_data))
    print("Data transformed and saved to 'data/transformed_data.csv'")
    print(transformed_data.head())