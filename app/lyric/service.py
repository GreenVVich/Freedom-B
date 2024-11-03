from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.lyric.models import Author, Collection, CollectionPoem, Poem
from app.lyric.schemas import (SAuthor, SCollection, SCollectionsByAuthor, SNewAuthor, SNewCollection, SNewPoem,
                               SPoemInCollection, SPoemsByCollection)


async def add_new_author(new_author: SNewAuthor, session: AsyncSession) -> SAuthor:
    author = Author(**new_author.model_dump())
    session.add(author)
    await session.commit()
    return author


async def add_new_collection(new_collection: SNewCollection, session: AsyncSession) -> SCollection:
    author = await session.get(Author, new_collection.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    collection = Collection(**new_collection.model_dump())
    session.add(collection)
    await session.commit()
    return collection


async def add_new_poem(new_poem: SNewPoem, session: AsyncSession) -> SPoemInCollection:
    author = await session.get(Author, new_poem.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")

    poem = Poem(author_id=new_poem.author_id, name=new_poem.name,
                content=new_poem.content, create_date=new_poem.create_date)
    session.add(poem)
    await session.flush()
    idx = None
    if new_poem.collection_id:
        result = await session.execute(
            select(func.coalesce(func.max(CollectionPoem.idx), 0) + 1)
            .where(CollectionPoem.collection_id == new_poem.collection_id))
        idx = result.scalar()
        if idx > 100:
            raise HTTPException(
                status_code=409, detail="Превышен лимит для одного альбома")

        connection = CollectionPoem(
            collection_id=new_poem.collection_id, poem_id=poem.id, idx=idx)
        session.add(connection)

    await session.commit()
    return SPoemInCollection(id=poem.id, idx=idx, **new_poem.model_dump())


async def get_collections_by_authors(session: AsyncSession) -> list[SCollectionsByAuthor]:
    # Limit and offset

    author_query = select(Author)
    authors = (await session.execute(author_query)).scalars().all()
    if not authors:
        raise HTTPException(status_code=404, detail="Авторы не найдены")

    collection_query = select(Collection).order_by(
        Collection.idx, Collection.id)
    collections = (await session.execute(collection_query)).scalars().all()
    if not collections:
        raise HTTPException(status_code=404, detail="Альбомы не найдены")

    result = []
    for author in authors:
        result.append(SCollectionsByAuthor(
            author=author,
            collections=[collection for collection in collections if collection.author_id == author.id]))
    return result


async def get_all_collections_by_author(author_id: int, session: AsyncSession) -> SCollectionsByAuthor:
    author = await session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    if author.deleted:
        raise HTTPException(status_code=410, detail="Автор был удалён")

    collections_query = (select(Collection)
                         .where(Collection.author_id == author.id)
                         .where(Collection.deleted.is_(False))
                         .order_by(Collection.idx, Collection.id))
    collections = (await session.execute(collections_query)).scalars().all()
    if not collections:
        raise HTTPException(status_code=404, detail="Альбомы не найдены")

    return SCollectionsByAuthor(author=author, collections=collections)


async def get_all_poems_by_collection(collection_id: int, session: AsyncSession) -> SPoemsByCollection:
    collection = await session.get(Collection, collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Альбом не найден")
    if collection.deleted:
        raise HTTPException(status_code=410, detail="Альбом был удалён")

    author = await session.get(Author, collection.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Автор не найден")
    if author.deleted:
        raise HTTPException(status_code=410, detail="Автор был удалён")

    pre_poems_query = (select(Poem, CollectionPoem.idx)
                       .select_from(Poem)
                       .join(CollectionPoem)
                       .where(CollectionPoem.collection_id == collection.id)
                       .where(Poem.deleted.is_(False))
                       .order_by(CollectionPoem.idx, Poem.id))
    pre_poems = (await session.execute(pre_poems_query)).all()
    return SPoemsByCollection(author=SAuthor(**author.__dict__),
                              collection=SCollection(**collection.__dict__),
                              poems=[{**poem.__dict__, "idx": idx} for poem, idx in pre_poems])


async def delete_full_poem(poem_id: int, session: AsyncSession) -> None:
    poem = await session.get(Poem, poem_id)
    if not poem:
        raise HTTPException(status_code=404, detail="Произведение не найдено")
    poem.deleted = True
    await session.commit()
    # TODO add return
