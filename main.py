from fastapi import FastAPI

from database.db import engine
from models.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Travel Service Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Travel Service Platform"
    }