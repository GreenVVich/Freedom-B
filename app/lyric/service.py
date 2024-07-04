from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.lyric.models import Author, Collection, CollectionPoem, Poem
from app.lyric.schemas import (SAuthor, SCollection, SCollectionsByAuthor, SNewAuthor, SNewCollection, SNewPoem, SPoem,
                               SPoemsByCollection)


async def add_new_author(new_author: SNewAuthor, session: AsyncSession) -> SAuthor:
    author = Author(**new_author.model_dump())
    session.add(author)
    await session.commit()
    return author


async def add_new_collection(new_collection: SNewCollection, session: AsyncSession) -> SCollection:
    collection = Collection(**new_collection.model_dump())
    session.add(collection)
    await session.commit()
    return collection


async def add_new_poem(new_poem: SNewPoem, session: AsyncSession) -> SPoem:
    poem = Poem(author_id=new_poem.author_id, name=new_poem.name,
                content=new_poem.content, version=new_poem.version,
                create_date=new_poem.create_date)
    session.add(poem)
    await session.flush()
    if new_poem.collection_id:
        connection = CollectionPoem(
            collection_id=new_poem.collection_id, poem_id=poem.id, idx=1)  # TODO idx gen
        session.add(connection)
    await session.commit()
    return poem


async def get_collections_by_authors(session: AsyncSession) -> list[SCollectionsByAuthor]:
    # TODO Исправить на один нормальный запрос, пушто стыдно, ей богу
    author_query = select(Author)
    authors = (await session.execute(author_query)).scalars().all()
    collection_query = select(Collection)
    collections = (await session.execute(collection_query)).scalars().all()
    result = []
    for author in authors:
        result.append({"author": author,
                       "collections": [collection for collection in collections if collection.author_id == author.id]})

    return result


async def get_all_collections_by_author(author_id: int, session: AsyncSession) -> SCollectionsByAuthor:
    author = await session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")

    collections_query = select(Collection).where(Collection.author_id == author.id).order_by(Collection.idx,
                                                                                             Collection.id)
    collections = (await session.execute(collections_query)).scalars().all()
    result = {"author": author, "collections": collections}
    return result


async def get_all_poems_by_collection(collection_id: int, session: AsyncSession) -> SPoemsByCollection:
    collection = await session.get(Collection, collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Альбом не найден")

    poems_query = (select(Poem).join(CollectionPoem)
                   .where(CollectionPoem.collection_id == collection.id)
                   .order_by(CollectionPoem.idx, Poem.id))
    poems = (await session.execute(poems_query)).scalars().all()
    author = await session.get(Author, collection.author_id)
    result = {"author": author, "collection": collection, "poems": poems}
    return result
