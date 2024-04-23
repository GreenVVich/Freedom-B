from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from settings import settings

engine = create_engine(url=settings.db_url, echo=True)

async_engine = create_async_engine(url=settings.db_url_async, echo=True)
