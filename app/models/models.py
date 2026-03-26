from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm.attributes import Mapped

engine = create_async_engine('postgresql+asyncpg://postgres:Admin@localhost:5432/sqlAlchemyTest', echo=False)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase): pass


class Users(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    email:Mapped[int] = mapped_column(String, unique=True)
    password:Mapped[int] = mapped_column(String)
class Trip(Base):
    __tablename__ = 'races'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    from_sity:Mapped[int] = mapped_column(String)
    to_city:Mapped[int] = mapped_column(String)
    price:Mapped[float] = mapped_column(String)
class Booking(Base):
    __tablename__ = 'order'
    id:Mapped[int]=mapped_column(String, primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    trip_id:Mapped[int] = mapped_column(ForeignKey('trip.id'))