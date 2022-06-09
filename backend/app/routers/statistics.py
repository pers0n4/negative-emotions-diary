from itertools import groupby
from operator import itemgetter

from app.core.auth import get_current_user
from app.models.diary import Diary
from app.models.user import User
from fastapi import APIRouter, Depends, status

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
)


@router.get("/affects", status_code=status.HTTP_200_OK)
async def read_affects(
    current_user: User = Depends(get_current_user),
):
    diaries = (
        await Diary.filter(user_id=current_user.id)
        .order_by("affect")
        .values("id", "content", "affect", "created_at", "updated_at")
    )

    return dict((k, list(g)) for k, g in groupby(diaries, key=itemgetter("affect")))
