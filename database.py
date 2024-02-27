from db_config import settings

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from asyncio import run

engine = create_engine(url=settings.db_url, echo=True)

async_engine = create_async_engine(url=settings.db_url_async, echo=True)


def sync_select():
    print('Начало')
    with engine.connect() as con:
        query = text("SELECT * FROM public.text_collector")
        res = con.execute(query).all()
        print(f"{res=}")
    print('Конец')


async def async_select():
    print('Начало')
    async with async_engine.connect() as con:
        print('\nПосле подключения к контекстному менеджеру')
        query = text("SELECT * FROM text_collector")
        res = await con.execute(query)
        print('\nПосле выполнения запроса')
        res = res.fetchmany(20)
        print(f"{res=}")
    print('\nКонец')

run(async_select())
