from app.core.auth import create_access_token, verify_password
from app.models.user import User
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/token")
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {
        "access_token": create_access_token(user.id),
        "token_type": "Bearer",
    }
