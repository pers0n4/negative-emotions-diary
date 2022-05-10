from app.core.auth import get_current_user
from app.models.diary import Diary
from app.models.user import User
from app.schemas.diary import DiaryCreate, DiaryRead
from fastapi import APIRouter, Depends, Query, status

router = APIRouter(
    prefix="/diaries",
    tags=["diaries"],
)


@router.get("", response_model=list[DiaryRead], status_code=status.HTTP_200_OK)
async def read_diarys(
    limit: int = Query(default=100, le=100),
    offset: int = 0,
    current_user: User = Depends(get_current_user),
):
    diarys = await Diary.filter(user_id=current_user.id).limit(limit).offset(offset)
    return diarys


@router.post("", response_model=DiaryRead, status_code=status.HTTP_201_CREATED)
async def create_diary(
    diary_body: DiaryCreate,
    current_user: User = Depends(get_current_user),
):
    diary = await Diary.create(
        **diary_body.dict(exclude_unset=True), user_id=current_user.id
    )
    return diary
