from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    age: int
    name: str


@app.post("/users/")
async def create_user(user: User):
    return {"id": 1, "age": user.age, "name": user.name}


if __name__ == "__main__":
    import uvicorn

    # Run the application with: uvicorn post_fastapi:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)
