from sqlalchemy import VARCHAR, Column, Integer

from app.database import Base


class Categories(Base):
    __tablename__ = "categories"

    categories_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, unique=True)
