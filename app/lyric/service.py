from sqlalchemy import text, select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.lyric.schemas import *
from app.lyric.models import *


async def get_all_tests(session: AsyncSession,) -> list[STestSchema]:
    query = text('''SELECT * FROM text_collector''')
    res = await session.execute(query)
    res = res.all()
    return res


async def add_new_author(new_author: SNewAuthor, session: AsyncSession) -> SAuthor:
    author = Author(pseudonym=new_author.pseudonym, info=new_author.info)
    session.add(author)
    await session.commit()
    return author


async def add_new_album(new_album: SNewAlbum, session: AsyncSession) -> SAlbum:
    # stmt =
    return ...


async def add_new_poem(new_poem: SNewPoem, session: AsyncSession) -> SPoem:
    # stmt =
    return ...

