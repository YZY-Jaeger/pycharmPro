# coding=utf-8
from sqlalchemy import Column, String, Integer, orm
from app.models.human import Human


class Jaeger(Human):
    id = Column(Integer, primary_key=True, autoincrement=True)
    college = Column(String(50), nullable=False)

    def __init__(self, name, age, college, email, password):
        super(Jaeger, self).__init__(name, age, email, password)
        self.college = college

    def jsonstr(self):

        jsondata = {
            'name': self.name,
            'age': self.age,
            'college': self.college,
            'email': self.email
        }

        return jsondata
