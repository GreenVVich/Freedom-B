from typing import Annotated
from fastapi import APIRouter, Depends

from app.poetry.schemas import SNewCreation, SCreation

creation_router = APIRouter(prefix='/creation', tags=['Авторское творчество'])


@creation_router.post('', response_model=SCreation)
def add_creation(new_creation: Annotated[SNewCreation, Depends()]) -> SCreation:
    # FIXME
    creation = SCreation(id=1, deleted=False, name=new_creation.name,
                         content=new_creation.content, author=new_creation.author, album=new_creation.album)
    return creation


@creation_router.get('')
def test_get() -> list[SCreation]:
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='test', content='content', author=i, album=1, deleted=False)
        lst.append(one)
    return lst


@creation_router.get('/by_author/{author_id}', response_model=list[SCreation])
def read_author_creations(author_id: int) -> list[SCreation]:
    # FIXME
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='author_test', content='content', author=author_id, album=1, deleted=False)
        lst.append(one)
    return lst


@creation_router.get('/by_album/{album_id}')
def read_album_creations(album_id: int) -> list[SCreation]:
    # FIXME
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='album_test', content='content', author=1, album=album_id, deleted=False)
        lst.append(one)
    return lst


@creation_router.get('/all')
def read_all_creations() -> list[SCreation]:
    # FIXME
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='test', content='content', author=i, album=1, deleted=False)
        lst.append(one)
    return lst
