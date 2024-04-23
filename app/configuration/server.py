from fastapi import FastAPI

from app.configuration.middlewares import __middlewares__
from app.configuration.routes import __routes__


class Server:
    __app: FastAPI

    def __init__(self):
        self.__app = FastAPI()
        self.__register_routes(self.__app)
        self.__register_middlewares(self.__app)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_routes(app):
        __routes__.register_routes(app)

    @staticmethod
    def __register_middlewares(app):
        __middlewares__.register_middlewares(app)
