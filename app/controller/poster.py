
from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.poster import Poster

posterBP = Blueprint('poster', __name__)


@posterBP.route('', methods=['GET'])
def insert_image(self, image):
    sql = "insert into picture(image) values(%s)"
    self.cursor.execute(sql, image)
    self.connection.commit()
