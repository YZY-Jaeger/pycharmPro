from sqlalchemy import Column, String, Integer, orm
from app.models.human import Human

class users(Human):

    def __init__(self, id, username, email, password):
        super(users,self).__init__(id,username,email, password)

