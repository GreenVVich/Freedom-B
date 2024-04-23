try:
    import uvicorn
except ImportError:
    import sys
    sys.exit('LOOK AT README...')

from app.configuration.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=str(settings.APP_HOST),
        port=int(settings.APP_PORT),
        log_level='trace' if not settings.DEVELOPMENT else 'debug',
        reload=True,
        factory=True,
    )
