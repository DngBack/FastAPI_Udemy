from typing import Annotated

from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends
import models
from models import Todos
from create_db import engine, SessionLocal


#  Set app 
app = FastAPI()

# Create database
models.Base.metadata.create_all(bind=engine)

def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()
