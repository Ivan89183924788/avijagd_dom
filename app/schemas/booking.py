from pydantic import BaseModel

class Booking(BaseModel):
    user_id:int
    trip_id:int