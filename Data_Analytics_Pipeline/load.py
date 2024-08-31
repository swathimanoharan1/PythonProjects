from sqlalchemy import create_engine

def load_data_to_db(data, db_uri):
    engine = create_engine(db_uri)
    data.to_sql('transformed_data', con=engine, if_exists = 'replace', index=False)

if __name__ == '__main__':
    from transform import transform_data
    from extract import extract_data

    raw_data = extract_data('data/raw_data.csv')
    transformed_data = transform_data(raw_data)
    load_data_to_db(transformed_data, 'sqlite:///data/analytics.db')
    print("Data load to database")
