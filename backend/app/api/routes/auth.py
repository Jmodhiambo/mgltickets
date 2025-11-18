from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from app.core.security import AuthUser, get_current_user
from app.core.config import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def create_access_token(data: Dict[str, Any], expires_minutes: int = 60) -> str:
    """Create a signed JWT."""
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate user and return JWT.
    Replace this dummy authentication with database lookup.
    """

    # Dummy users for testing – replace with DB
    fake_users = {
        "admin@example.com": {"id": "1", "password": "adminpass", "role": "admin"},
        "user@example.com": {"id": "2", "password": "userpass", "role": "user"},
    }

    user_data = fake_users.get(form.username)
    if not user_data or user_data["password"] != form.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "user_id": user_data["id"],
        "role": user_data["role"],
    }

    access_token = create_access_token(token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 3600,
        "user": {
            "id": user_data["id"],
            "role": user_data["role"],
        },
    }


@router.post("/refresh")
async def refresh_token(user: AuthUser = Depends(get_current_user)):
    """
    Generate a fresh JWT for an authenticated user.
    """

    if not user:
        raise HTTPException(status_code=401, detail="Authentication required")

    token_data = {
        "user_id": user.id,
        "role": user.role,
    }

    new_token = create_access_token(token_data)

    return {
        "access_token": new_token,
        "token_type": "bearer",
        "expires_in": 3600,
        "user": {
            "id": user.id,
            "role": user.role,
        },
    }