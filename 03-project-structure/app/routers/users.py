from uuid import UUID

import bcrypt
from fastapi import APIRouter

from ..models.users import CreateUserRequest, CreateUserResponse, GetUserResponse, User


db = dict()  # fake database

router = APIRouter()


@router.post("/users/")
async def create_user(user: CreateUserRequest) -> CreateUserResponse:
    user = User(**user.model_dump())
    user.password = bcrypt.hashpw(user.password, bcrypt.gensalt())
    db[user.id] = user
    return user


@router.get("/users/{id}")
async def get_user(id: UUID) -> GetUserResponse | dict:
    return db.get(id, dict())


@router.get("/users/")
async def list_users() -> list[GetUserResponse] | list:
    return db.values()


#
# The routes below are for demo purposes
#
@router.get("/users/raw/{id}", tags=["raw"])
async def get_raw_user(id: UUID) -> User | dict:
    return db.get(id, dict())


@router.get("/users/raw/", tags=["raw"])
async def list_raw_users() -> list[User] | list:
    return db.values()
