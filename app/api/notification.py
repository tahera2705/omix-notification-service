from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.db.dependencies import get_db
from app.models.notification import Notification
from app.schemas.notification import (
    NotificationCreate,
    NotificationResponse,
    NotificationUpdate
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post(
    "/",
    response_model=NotificationResponse
)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    new_notification = Notification(
        title=notification.title,
        message=notification.message,
        channel=notification.channel
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification


@router.get(
    "/",
    response_model=list[NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    notifications = db.query(
        Notification
    ).all()

    return notifications


@router.get("/search/")
def search_notifications(
    title: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    notifications = db.query(
        Notification
    ).filter(
        Notification.title.contains(title)
    ).all()

    return notifications


@router.get("/status/")
def filter_notifications_by_status(
    status: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    notifications = db.query(
        Notification
    ).filter(
        Notification.status == status
    ).all()

    return notifications


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    notification = db.query(
        Notification
    ).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


@router.put(
    "/{notification_id}",
    response_model=NotificationResponse
)
def update_notification(
    notification_id: int,
    notification_update: NotificationUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    notification = db.query(
        Notification
    ).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    notification.status = notification_update.status

    db.commit()
    db.refresh(notification)

    return notification


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    notification = db.query(
        Notification
    ).filter(
        Notification.id == notification_id
    ).first()

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification deleted successfully"
    }