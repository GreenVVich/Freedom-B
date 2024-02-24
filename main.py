from fastapi import FastAPI

from router import router as creation_router

app = FastAPI()
app.include_router(creation_router)
