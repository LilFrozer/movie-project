
# Created by Геннадий on 28.02.2026.

#venv\Scripts\activate
#uvicorn main:app --reload

from fastapi import FastAPI
from api.routers import auth, users, verify

app = FastAPI()

app.include_router(auth.router, prefix="/api")