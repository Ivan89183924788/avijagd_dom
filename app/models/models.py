

from sqlalchemy.orm import DeclarativeBase, mapped_column,Mapped
from sqlalchemy import String, ForeignKey,Float




class Base(DeclarativeBase): pass


class User(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    email:Mapped[int] = mapped_column(String, unique=True)
    password:Mapped[int] = mapped_column(String)
class Trip(Base):
    __tablename__ = 'trips'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    from_sity:Mapped[int] = mapped_column(String)
    to_city:Mapped[int] = mapped_column(String)
    price:Mapped[float] = mapped_column(String)
class Booking(Base):
    __tablename__ = 'bookings'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    trip_id:Mapped[int] = mapped_column(ForeignKey('trips.id'))