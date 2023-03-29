from sqlalchemy.orm import sessionmaker
from .database import engine

from . import schemas
from . import models

models.Base.metadata.create_all(bind=engine)


"""This method receives login, email and phone of user,
   create new models.User object with this data and put 
   this object into database. 
   After all, this method returns an ID of new user"""
def add_user(user: schemas.User):
    db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = db()
    db_user = models.User(name=user.name)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_id(user_id: int):
    db = sessionmaker(bind=engine)
    session = db()
    user = session.query(models.User).filter(models.User.id == user_id).first()
    return user