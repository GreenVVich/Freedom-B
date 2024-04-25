from pydantic import BaseModel


class STestSchema(BaseModel):
    id: int
    info: str


class SNewAuthor(BaseModel):
    pseudonym: str
    info: str | None


class SAuthor(BaseModel):
    id: int
    deleted: bool
    pseudonym: str
    info: str


class SNewAlbum(BaseModel):
    name: str
    author: int


class SAlbum(BaseModel):
    id: int
    deleted: bool
    name: str
    author: int | None


class SNewPoem(BaseModel):
    name: str
    content: str
    author: int | None
    album: int | None


class SPoem(BaseModel):
    id: int
    deleted: bool
    name: str
    content: str
    author: int | None
    album: int | None
