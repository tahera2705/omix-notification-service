from fastapi import FastAPI

from app.db.database import engine, Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Omix Notification Service",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Omix Notification Service API is running"
    }