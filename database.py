from db_config import settings

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from asyncio import run

engine = create_engine(
    url=settings.db_url,
    echo=True)

async_engine = create_async_engine(
    url=settings.db_url_async,
    echo=True)

# with engine.connect() as con:
#     query = text("SELECT * FROM public.text_collector")
#     res = con.execute(query).all()
#     # con.commit()
#     print(f"{res=}")


async def async_select():
    async with async_engine.connect() as con:
        query = text("SELECT * FROM text_collector")
        res = await con.execute(query)
        res = res.all()
        # con.commit()
        print(f"{res=}")

run(async_select())
