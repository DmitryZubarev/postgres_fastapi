from fastapi import FastAPI

from . import db_api, models, schemas
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/registrate")
async def check(user: schemas.User):
    new_user = db_api.add_user(user)
    return {'id': new_user.id}


@app.get("/users/{user_id}")
async def users(user_id: int):
    user = db_api.get_user_by_id(user_id)
    if user is None:
        return None
    return {'id': user.id, 'name': user.name}