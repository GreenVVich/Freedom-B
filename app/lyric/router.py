from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.configuration.database import get_async_session
from app.lyric.schemas import *
from app.lyric.service import get_all_tests, add_new_author, add_new_album, add_new_poem, get_all_authors, \
    get_all_albums, get_all_poems, get_all_poems_by_album

lyric_router = APIRouter(prefix='/lyrics', tags=['Авторское творчество'])


@lyric_router.post('/authors', response_model=SAuthor)
async def add_author(new_author: Annotated[SNewAuthor, Depends()],
                     session: AsyncSession = Depends(get_async_session)) -> SAuthor:
    return await add_new_author(new_author, session)


@lyric_router.get('/authors', response_model=list[SAuthor])
async def get_authors(session: AsyncSession = Depends(get_async_session)) -> list[SAuthor]:
    return await get_all_authors(session)


@lyric_router.post('/albums', response_model=SAlbum)
async def add_album(new_album: Annotated[SNewAlbum, Depends()],
                    session: AsyncSession = Depends(get_async_session)) -> SAlbum:
    return await add_new_album(new_album, session)


@lyric_router.get('/albums', response_model=list[SAlbum])
async def get_albums(session: AsyncSession = Depends(get_async_session)) -> list[SAlbum]:
    return await get_all_albums(session)


@lyric_router.post('/poems', response_model=SPoem)
async def add_poem(new_poem: SNewPoem,
                   session: AsyncSession = Depends(get_async_session)) -> SPoem:
    return await add_new_poem(new_poem, session)


@lyric_router.get('/poems', response_model=list[SPoem])
async def get_poems(session: AsyncSession = Depends(get_async_session)) -> list[SPoem]:
    return await get_all_poems(session)


@lyric_router.get('/albums/{album_id}', response_model=SPoemsByAlbum)
async def get_poems_by_album(album_id: int, session: AsyncSession = Depends(get_async_session)):
    return await get_all_poems_by_album(album_id, session)


@lyric_router.get('/test', response_model=list[STestSchema])
async def get_test(session: AsyncSession = Depends(get_async_session)) -> list[STestSchema]:
    return await get_all_tests(session)
