from fastapi import FastAPI
from app.database import engine
from app.routers import auth, blogs, users
from app.database import generate_missing_tables

app = FastAPI()

# create table if not already existing
generate_missing_tables()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(blogs.router)
