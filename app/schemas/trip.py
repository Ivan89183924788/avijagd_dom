from pydantic import BaseModel

class Tripcreate(BaseModel):
    from_sity:str
    to_sity:str
    price:float