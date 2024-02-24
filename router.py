from typing import Annotated
from fastapi import APIRouter, Depends

from schemas import SNewCreation, SCreation

router = APIRouter(prefix='/creation', tags=['Авторское творчество'])


@router.post('')
def add_creation(creation: Annotated[SNewCreation, Depends()]) -> SNewCreation:
    # FIXME
    return creation


@router.get('')
def test_get() -> list[SCreation]:
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='test', content='content', author=i, album=1, deleted=False)
        lst.append(one)
    return lst


@router.get('/by_author/{author_id}')
def read_author_creations(author_id: int) -> list[SCreation]:
    # FIXME
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='author_test', content='content', author=author_id, album=1, deleted=False)
        lst.append(one)
    return lst


@router.get('/by_album/{album_id}')
def read_album_creations(album_id: int) -> list[SCreation]:
    # FIXME
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='album_test', content='content', author=1, album=album_id, deleted=False)
        lst.append(one)
    return lst


@router.get('')
def read_all_creations() -> list[SCreation]:
    # FIXME
    lst = []
    for i in range(3):
        one = SCreation(id=i+1, name='test', content='content', author=i, album=1, deleted=False)
        lst.append(one)
    return lst
