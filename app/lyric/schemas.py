from datetime import datetime

from pydantic import BaseModel


class SNewAuthor(BaseModel):
    pseudonym: str
    info: str | None = None


class SAuthor(BaseModel):
    id: int
    deleted: bool
    pseudonym: str
    info: str | None


class SNewCollection(BaseModel):
    author_id: int
    name: str
    description: str | None = None
    publish_date: datetime | None = datetime.now()


class SCollection(BaseModel):
    id: int
    deleted: bool
    author_id: int
    idx: int
    name: str
    description: str | None
    publish_date: datetime


class SNewPoem(BaseModel):
    author_id: int
    collection_id: int | None = None
    name: str
    content: str
    parent_id: int | None = None
    create_date: datetime | None = datetime.now()


class SPoemInCollection(BaseModel):
    id: int
    idx: int | None
    deleted: bool
    author_id: int
    name: str
    content: str
    parent_id: int | None
    create_date: datetime


class SPoemsByCollection(BaseModel):
    author: SAuthor
    collection: SCollection
    poems: list[SPoemInCollection]


class SCollectionsByAuthor(BaseModel):
    author: SAuthor
    collections: list[SCollection]
