from sqlalchemy import Column, String, Integer, orm
from app.models.base import Base



class Human(Base):
    __abstract__ = True # 抽象类 不会生成表
    id = Column(String(50), nullable=False, primary_key= True)
    username = Column(String(35))
    email = Column(String(24), unique=True, nullable=True)
    password = Column('password', String(100))


    def __init__(self, username, email, password):
        super(Human,self).__init__()
        self.id = id
        self.username = username
        self.email = email
        self.password = password
