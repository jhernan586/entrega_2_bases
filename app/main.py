from fastapi import FastAPI
from app.routes import router
from pydantic import BaseModel
app = FastAPI()

app.include_router(router)