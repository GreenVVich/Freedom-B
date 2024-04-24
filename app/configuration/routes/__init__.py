from app.configuration.routes.routes import Routes
from app.lyric.router import lyric_router

__routes__ = Routes(
    routers=(lyric_router,)
)
