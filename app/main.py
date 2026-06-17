from fastapi import FastAPI
from app.api.notification import (
    router as notification_router
)

from app.db.database import engine, Base
from app.models.user import User
from app.models.notification import Notification
from app.api.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Omix Notification Service",
    version="1.0.0",
    debug=True
)
app.include_router(user_router)
app.include_router(notification_router)

@app.get("/")
def root():
    return {
        "message": "Omix Notification Service API is running"
    }