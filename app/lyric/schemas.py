from datetime import datetime

from pydantic import BaseModel


class SNewAuthor(BaseModel):
    pseudonym: str
    info: str | None = None


class SAuthor(BaseModel):
    id: int
    deleted: bool
    pseudonym: str
    info: str


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
    description: str | None = None
    publish_date: datetime


class SNewPoem(BaseModel):
    collection_id: int
    name: str
    content: str
    create_date: datetime | None = datetime.now()


class SPoem(BaseModel):
    id: int
    deleted: bool
    collection_id: int
    idx: int
    name: str
    content: str
    create_date: datetime


class SPoemsByCollection(BaseModel):
    author: SAuthor
    collection: SCollection
    poems: list[SPoem]


class SCollectionsByAuthor(BaseModel):
    author: SAuthor
    collections: list[SCollection]
