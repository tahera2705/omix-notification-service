from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    Token
)
from app.util.security import (
    hash_password,
    verify_password
)
from app.core.auth import create_access_token

router = APIRouter(tags=["Users"])


@router.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=Token)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token_data = {
        "sub": str(db_user.id)
    }

    access_token = create_access_token(
        token_data
    )

    return Token(
        access_token=access_token,
        token_type="bearer"
    )