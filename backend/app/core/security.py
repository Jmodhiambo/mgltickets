from typing import Optional, Dict, Any
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.config import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError
from dataclasses import dataclass


@dataclass
class AuthUser:
    id: str
    role: str


bearer_scheme = HTTPBearer(auto_error=False)


def decode_jwt(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY.get_secret_value(), algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


async def get_current_user(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme)
) -> Optional[AuthUser]:

    # No token provided → treat as anonymous
    if credentials is None:
        request.state.user = None
        return None

    token = credentials.credentials
    payload = decode_jwt(token)

    user_id = payload.get("user_id")
    role = payload.get("role")

    if not user_id:
        raise HTTPException(status_code=401, detail="Missing user_id in token")

    user = AuthUser(id=str(user_id), role=str(role or "user"))

    # Attach user to request state → picked up by logging middleware
    request.state.user = user

    return user
