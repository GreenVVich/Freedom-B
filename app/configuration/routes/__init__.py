from app.configuration.routes.routes import Routes
from app.poetry.router import creation_router

__routes__ = Routes(
    routers=(creation_router,)
)
