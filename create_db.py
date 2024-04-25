from asyncio import run

from app.configuration.database import create_tables

run(create_tables())
