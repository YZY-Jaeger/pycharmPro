from sqlalchemy import Column, String, Integer, orm, LargeBinary
from app.models.base import Base

class Poster(Base):

    id = Column(String(50), nullable=False, primary_key= True)
    name = Column(String(35))
    pic = Column(LargeBinary)
    votes = Column(Integer)



