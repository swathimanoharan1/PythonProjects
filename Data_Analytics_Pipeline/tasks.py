from celery import Celery

app = Celery("tasks", broker="memory://")

@app.task
def run_pipeline():
    from extract import extract_data
    from transform import transform_data
    from load import load_data_to_db

    raw_data = extract_data("data/raw_data.csv")
    transformed_data = transform_data(raw_data)
    load_data_to_db(transformed_data, "sqlite:///data/analytics.db")

if __name__ == "__main__":
    run_pipeline.apply_async()