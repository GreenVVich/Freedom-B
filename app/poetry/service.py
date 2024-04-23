from asyncio import run

from sqlalchemy import text

from app.configuration.database import async_engine, engine


def sync_select():
    print('Начало')
    with engine.connect() as con:
        query = text("SELECT * FROM text_collector")
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
