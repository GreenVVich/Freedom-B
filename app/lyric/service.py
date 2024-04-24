from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.lyric.schemas import SPoem, STestSchema, SNewPoem


async def add_new_poem(new_poem: SNewPoem, session: AsyncSession) -> SPoem:
    return ...


async def get_all_poems(session: AsyncSession,) -> list[STestSchema]:
    query = text('''SELECT * FROM text_collector''')
    res = await session.execute(query)
    res = res.all()
    return res

