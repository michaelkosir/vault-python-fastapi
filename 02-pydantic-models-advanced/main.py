from datetime import datetime, timezone
from uuid import UUID, uuid4

import bcrypt
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, EmailStr, Field

app = FastAPI(docs_url="/")

db = dict()  # fake database


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0, lt=200)
    password: str = Field(min_length=8, max_length=128)
    ccn: str = Field(pattern=r"^\d{4}-\d{4}-\d{4}-\d{4}$")
    ssn: str = Field(pattern=r"^\d{3}-\d{2}-\d{4}$")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "name": "John Doe",
                    "age": 42,
                    "email": "foobar@example.com",
                    "password": "4D814A97-95B3-4F",
                    "ccn": "4111-1111-1111-1111",
                    "ssn": "123-45-6789",
                }
            ]
        }
    )


class User(CreateUserRequest):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    password: bytes


class CreateUserResponse(BaseModel):
    id: UUID


class GetUserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    age: int


@app.post("/users/")
async def create_user(user: CreateUserRequest) -> CreateUserResponse:
    user = User(**user.model_dump())
    user.password = bcrypt.hashpw(user.password, bcrypt.gensalt())
    db[user.id] = user
    return user


@app.get("/users/{id}")
async def get_user(id: UUID) -> GetUserResponse | dict:
    return db.get(id, dict())


@app.get("/users/")
async def list_users() -> list[GetUserResponse] | list:
    return db.values()


#
# The routes below are for demo purposes
#
@app.get("/users/raw/{id}")
async def get_raw_user(id: UUID) -> User | dict:
    return db.get(id, dict())


@app.get("/users/raw/")
async def list_raw_users() -> list[User] | list:
    return db.values()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
