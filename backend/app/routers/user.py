from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from fastapi import APIRouter, HTTPException, Query, status

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("", response_model=list[UserRead], status_code=status.HTTP_200_OK)
async def read_users(limit: int = Query(default=100, le=100), offset: int = 0):
    users = await User.all().limit(limit).offset(offset)
    return users


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_body: UserCreate):
    user = await User.get_by_email(user_body.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists"
        )
    user = await User.create(**user_body.dict(exclude_unset=True))
    return user


from pydantic import BaseModel


class Test(BaseModel):
    id: str
    password: str


@router.post("/test")
async def read_user(body: Test):
    if body.id == "test" and body.password == "pass":
        return "hello"
    else:
        return "bye"
