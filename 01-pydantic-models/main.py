from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.post("/users/")
async def create_user(user: User):
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
