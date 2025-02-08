from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, EmailStr, Field


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


class CreateUserResponse(BaseModel):
    id: UUID


class GetUserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    age: int
