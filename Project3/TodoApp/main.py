from fastapi import FastAPI
import models
from create_db import engine


#  Set app 
app = FastAPI()

# Create database
models.Base.metadata.create_all(bind=engine)
