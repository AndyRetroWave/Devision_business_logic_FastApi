from sqlalchemy import DECIMAL, VARCHAR, Column, ForeignKey, Integer

from app.database import Base


class Sneakers(Base):
    __tablename__ = "sneakers"

    sneaker_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    brand_id = Column(Integer, ForeignKey("brands.brands_id"))
    category = Column(Integer, ForeignKey("categories.categories_id"))
    price = Column(DECIMAL, nullable=False)
    size = Column(VARCHAR)
    color = Column(VARCHAR)
    description = Column(VARCHAR)
    image_url = Column(VARCHAR)


class Categories(Base):
    __tablename__ = "categories"

    categories_id = Column(Integer, primary_key=True)
    name = Column(VARCHAR, unique=True)
