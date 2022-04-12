from datetime import datetime, timedelta
from typing import Any, Optional, Union

from app.models.user import User
from app.schemas.auth import JwtRegisteredClaim
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "SECRET"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    subject: Union[str, Any], expires_delta: Optional[timedelta] = None
):
    now = datetime.utcnow()
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=15)

    claims = {"sub": str(subject), "iat": now, "exp": expire}
    access_token = jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM)

    return access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        claims = JwtRegisteredClaim(**payload)
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await User.get(id=claims.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
