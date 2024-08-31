from tasks import run_pipeline

if __name__ == "__main__":
    result = run_pipeline.apply_async()
    print("Pipeline execution started")
    result.get()
    print("Pipeline execution completed")