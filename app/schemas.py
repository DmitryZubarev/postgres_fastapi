from pydantic import BaseModel


"""This class will be used to validate incoming json files on post request with path '/check ' """
class User(BaseModel):
    name: str