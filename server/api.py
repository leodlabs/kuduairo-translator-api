from fastapi import FastAPI
from .routes import router as TranslateRouter

app = FastAPI()

@app.get("/", tags=["Root Path"])
async def index():
    return { 'status': 'OK' }

app.include_router(TranslateRouter, prefix="/translate")