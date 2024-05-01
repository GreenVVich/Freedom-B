from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.configuration.database import get_async_session
from app.lyric.schemas import *
from app.lyric.service import add_new_author, add_new_album, add_new_poem, get_albums_by_authors, \
    get_all_poems_by_album, get_all_albums_by_author, get_all_tests

lyric_router = APIRouter(prefix='/lyrics', tags=['Авторское творчество'])


@lyric_router.post('/authors', response_model=SAuthor)
async def add_author(new_author: Annotated[SNewAuthor, Depends()],
                     session: AsyncSession = Depends(get_async_session)) -> SAuthor:
    return await add_new_author(new_author, session)


@lyric_router.post('/albums', response_model=SAlbum)
async def add_album(new_album: Annotated[SNewAlbum, Depends()],
                    session: AsyncSession = Depends(get_async_session)) -> SAlbum:
    return await add_new_album(new_album, session)


@lyric_router.post('/poems', response_model=SPoem)
async def add_poem(new_poem: SNewPoem,
                   session: AsyncSession = Depends(get_async_session)) -> SPoem:
    return await add_new_poem(new_poem, session)


@lyric_router.get('/', response_model=list[SAlbumsByAuthor])
async def welcome(session: AsyncSession = Depends(get_async_session)) -> list[SAlbumsByAuthor]:
    return await get_albums_by_authors(session)


@lyric_router.get('/authors/{author_id}', response_model=SAlbumsByAuthor)
async def get_albums_by_author(author_id: int, session: AsyncSession = Depends(get_async_session)) -> SAlbumsByAuthor:
    return await get_all_albums_by_author(author_id, session)


@lyric_router.get('/albums/{album_id}', response_model=SPoemsByAlbum)
async def get_poems_by_album(album_id: int, session: AsyncSession = Depends(get_async_session)) -> SPoemsByAlbum:
    return await get_all_poems_by_album(album_id, session)


@lyric_router.get('/test', response_model=list[STestSchema])
async def get_test(session: AsyncSession = Depends(get_async_session)) -> list[STestSchema]:
    return await get_all_tests(session)
