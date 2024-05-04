from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.configuration.database import get_async_session
from app.lyric.schemas import *
from app.lyric.service import (add_new_author, add_new_collection, add_new_poem, get_all_collections_by_author,
                               get_all_poems_by_collection, get_collections_by_authors)

lyric_router = APIRouter(prefix='/lyrics', tags=['Авторское творчество'])


@lyric_router.post('/authors', response_model=SAuthor)
async def add_author(new_author: Annotated[SNewAuthor, Depends()],
                     session: AsyncSession = Depends(get_async_session)) -> SAuthor:
    return await add_new_author(new_author, session)


@lyric_router.post('/collections', response_model=SCollection)
async def add_collection(new_collection: Annotated[SNewCollection, Depends()],
                         session: AsyncSession = Depends(get_async_session)) -> SCollection:
    return await add_new_collection(new_collection, session)


@lyric_router.post('/poems', response_model=SPoem)
async def add_poem(new_poem: Annotated[SNewPoem, Depends()],
                   session: AsyncSession = Depends(get_async_session)) -> SPoem:
    return await add_new_poem(new_poem, session)


@lyric_router.get('/', response_model=list[SCollectionsByAuthor])
async def welcome(session: AsyncSession = Depends(get_async_session)) -> list[SCollectionsByAuthor]:
    return await get_collections_by_authors(session)


@lyric_router.get('/authors/{author_id}', response_model=SCollectionsByAuthor)
async def get_collections_by_author(author_id: int,
                                    session: AsyncSession = Depends(get_async_session)) -> SCollectionsByAuthor:
    return await get_all_collections_by_author(author_id, session)


@lyric_router.get('/collections/{collection_id}', response_model=SPoemsByCollection)
async def get_poems_by_collection(collection_id: int,
                                  session: AsyncSession = Depends(get_async_session)) -> SPoemsByCollection:
    return await get_all_poems_by_collection(collection_id, session)
