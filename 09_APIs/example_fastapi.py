from fastapi import FastAPI

app = FastAPI()


@app.get("/greet")
def greet_user():
    return {"message": "salam"}


if __name__ == "__main__":
    import uvicorn

    # Run the application with: uvicorn example_fastapi:app --reload
