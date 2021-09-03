from fastapi import FastAPI
from app.routers import auth, users
from app.database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
  create_db_and_tables()# create table if not already existing

app.include_router(auth.router)
app.include_router(users.router)
