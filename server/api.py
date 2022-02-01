from fastapi import FastAPI
from .routes import router as TranslateRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://kuduairo.netlify.app",
    "http://192.168.1.70:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root Path"])
async def index():
    return { 'status': 'OK' }

app.include_router(TranslateRouter, prefix="/translate")
