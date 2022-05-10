from app.core.auth import create_access_token, get_current_user, verify_password
from app.models.user import User
from app.schemas.user import UserRead
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/token")
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    return {
        "access_token": create_access_token(user.id),
        "token_type": "Bearer",
    }


@router.get(
    "/token", response_model=UserRead, status_code=status.HTTP_200_OK, tags=["auth"]
)
async def validate_token(user: User = Depends(get_current_user)):
    return user
