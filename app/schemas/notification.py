from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class ChannelEnum(str, Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"
    PUSH = "PUSH"


class StatusEnum(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"


class NotificationCreate(BaseModel):
    title: str
    message: str
    channel: ChannelEnum


class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    channel: ChannelEnum
    status: StatusEnum
    created_at: datetime

    class Config:
        from_attributes = True


class NotificationUpdate(BaseModel):
    status: StatusEnum