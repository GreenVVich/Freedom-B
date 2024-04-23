from fastapi import FastAPI

from app.configuration.server import Server


def app(_=None) -> FastAPI:
    return Server().get_app()
