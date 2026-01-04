from typing import Union
# from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
# from fastapi.params import Body
# from pydantic import BaseModel
# from random import randrange
# import time
# import psycopg2

# from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import get_db,engine, SessionLocal
from .routers import post, users, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
#from . import config

#(dont need because using alembic now)
#models.Base.metadata.create_all(bind = engine) 

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# def get_settings():
#     return config.settings()

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def read_root():
    return {"Hello": "Wellcom to FastApi updated"}
    
