from pydantic import BaseModel


class NotificationCreate(BaseModel):
    title: str
    message: str
    channel: str


class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    channel: str
    status: str

    class Config:
        from_attributes = True


class NotificationUpdate(BaseModel):
    status: str       