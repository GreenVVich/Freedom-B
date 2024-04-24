from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.configuration.database import get_async_session
from app.lyric.schemas import SNewPoem, SPoem, STestSchema
from app.lyric.service import get_all_poems, add_new_poem

lyric_router = APIRouter(prefix='/lyrics', tags=['Авторское творчество'])


@lyric_router.post('', response_model=SPoem)
async def add_poem(new_poem: Annotated[SNewPoem, Depends()],
                   session: AsyncSession = Depends(get_async_session)) -> SPoem:
    return await add_new_poem(new_poem, session)


@lyric_router.get('/test', response_model=list[STestSchema])
async def get_all(session: AsyncSession = Depends(get_async_session)) -> list[STestSchema]:
    return await get_all_poems(session)


