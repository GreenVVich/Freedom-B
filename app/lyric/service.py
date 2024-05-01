from fastapi import HTTPException
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.lyric.schemas import STestSchema, SNewAuthor, SAuthor, SNewAlbum, SAlbum, SNewPoem, SPoem, SPoemsByAlbum, \
    SAlbumsByAuthor
from app.lyric.models import Author, Album, Poem


async def add_new_author(new_author: SNewAuthor, session: AsyncSession) -> SAuthor:
    author = Author(pseudonym=new_author.pseudonym, info=new_author.info)
    session.add(author)
    await session.commit()
    return author


async def add_new_album(new_album: SNewAlbum, session: AsyncSession) -> SAlbum:
    album = Album(name=new_album.name, author_id=new_album.author_id)
    session.add(album)
    await session.commit()
    return album


async def add_new_poem(new_poem: SNewPoem, session: AsyncSession) -> SPoem:
    poem = Poem(album_id=new_poem.album_id, name=new_poem.name, content=new_poem.content)
    session.add(poem)
    await session.commit()
    return poem


async def get_albums_by_authors(session: AsyncSession) -> list[SAlbumsByAuthor]:
    # TODO Исправить на один нормальный запрос, пушто стыдно, ей богу
    author_query = select(Author)
    authors = (await session.execute(author_query)).scalars().all()
    album_query = select(Album)
    albums = (await session.execute(album_query)).scalars().all()
    result = []
    for author in authors:
        result.append({'author': author, 'albums': [album for album in albums if album.author_id == author.id]})

    return result


async def get_all_albums_by_author(author_id: int, session: AsyncSession) -> SAlbumsByAuthor:
    author = await session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")

    albums_query = select(Album).where(Album.author_id == author.id).order_by(Album.id)  # TODO idx / sort
    albums = (await session.execute(albums_query)).scalars().all()
    result = {'author': author, 'albums': albums}
    return result


async def get_all_poems_by_album(album_id: int, session: AsyncSession) -> SPoemsByAlbum:
    album = await session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Альбом не найден")

    poems_query = select(Poem).where(Poem.album_id == album.id).order_by(Poem.id)  # TODO idx / sort
    poems = (await session.execute(poems_query)).scalars().all()
    author = await session.get(Author, album.author_id)
    result = {'author': author, 'album': album, 'poems': poems}
    return result


async def get_all_tests(session: AsyncSession,) -> list[STestSchema]:
    query = text('''SELECT * FROM text_collector''')
    res = await session.execute(query)
    res = res.all()
    return res