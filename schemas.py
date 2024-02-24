from pydantic import BaseModel


class SNewCreation(BaseModel):
    name: str
    content: str
    author: int | None
    album: int | None


class SCreation(SNewCreation):
    id: int
    deleted: bool


class SNewAlbum(BaseModel):
    name: str
    author: int


class SAlbum(SNewAlbum):
    id: int
    deleted: bool


class SNewAuthor(BaseModel):
    pseudonym: str
    info: str


class SAuthor(SNewAuthor):
    id: int
    deleted: bool
