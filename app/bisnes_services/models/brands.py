from sqlalchemy import VARCHAR, Column, Integer
from app.database import Base


class Brands(Base):
    __tablename__ = "brands"

    brands_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, unique=True)
    country = Column(VARCHAR)
