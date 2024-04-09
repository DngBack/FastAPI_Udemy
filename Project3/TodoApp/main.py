from typing import Annotated
from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from starlette import status

import models
from models import Todos
from create_db import engine, SessionLocal
from routers import auth, todos


#  Set app 
app = FastAPI()

# Create database
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
