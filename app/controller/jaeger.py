# coding=utf-8
from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.jaeger import Jaeger

jaegerBP = Blueprint('jaeger',__name__)


@jaegerBP.route('/', methods=['GET'])
def get_jaeger():
    with db.auto_commit():
        jaeger = Jaeger('YZY', 22, 'UIC', 'yzy@mail.uic.edu.cn', '123456')
        # 数据库的insert操作
        db.session.add(jaeger)
    return 'hello Jaeger'
