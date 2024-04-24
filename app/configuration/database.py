from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.configuration.settings import settings

Base = declarative_base()

metadata = MetaData()

engine = create_async_engine(url=settings.db_url_async, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

