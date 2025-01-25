from fastapi import FastAPI
from db.engine import Engine, Base


app = FastAPI()


Engine.connect()
Base.metadata.create_all(Engine)