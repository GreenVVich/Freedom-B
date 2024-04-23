from pydantic import BaseModel


class SNewCreation(BaseModel):
    name: str
    content: str
    author: int | None
    album: int | None


class SCreation(BaseModel):
    id: int
    deleted: bool
    name: str
    content: str
    author: int | None
    album: int | None


class SNewAlbum(BaseModel):
    name: str
    author: int


class SAlbum(BaseModel):
    id: int
    deleted: bool
    name: str
    author: int | None


class SNewAuthor(BaseModel):
    pseudonym: str
    info: str | None


class SAuthor(BaseModel):
    id: int
    deleted: bool
    pseudonym: str
    info: str
