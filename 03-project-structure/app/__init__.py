from fastapi import FastAPI

from .routers import users

app = FastAPI(docs_url="/")

app.include_router(users.router)
