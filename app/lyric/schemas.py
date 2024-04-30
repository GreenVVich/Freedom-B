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
    author_id: int
    name: str


class SAlbum(BaseModel):
    id: int
    deleted: bool
    author_id: int
    name: str


class SNewPoem(BaseModel):
    album_id: int
    name: str
    content: str


class SPoem(BaseModel):
    id: int
    deleted: bool
    album_id: int
    name: str
    content: str


class SPoemsByAlbum(BaseModel):
    author: SAuthor
    album: SAlbum
    poems: list[SPoem]


class SAlbumsByAuthor(BaseModel):
    author: SAuthor
    albums: list[SAlbum]
