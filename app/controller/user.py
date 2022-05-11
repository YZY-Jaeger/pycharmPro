# coding=utf-8
from flask import Blueprint,render_template, request, jsonify
from app.models.base import db
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.jaeger import Jaeger
from app.models.luckyDrawer import LuckyDrawer
from sqlalchemy import or_, and_, all_, any_

userBP = Blueprint('user', __name__)

@userBP.route('/')
def hello_world():
    return 'Hello, World!'
@userBP.route('/login',methods=['GET','POST'])

def login():
    if request.method == 'GET':
        return render_template('login.html',title='Sample Login',header='Sample Case')
    else:

        email = request.form.get('email')
        _password = request.form.get('password')

        print(email, _password)

        if '@mail.uic.edu.hk' in email: # 并不严谨，仅作测试，应该用正则
            result = Student.query.filter(and_(Student.email == email, Student._password == _password)).first()
            # tr = TimetableRecord.query.filter(and_(TimetableRecord.tid==tid, TimetableRecord.day == day,TimetableRecord.status!=2)).first()
            print(result.jsonstr())
        elif '@uic.edu.hk' in email:
            result = Teacher.query.filter(and_(Teacher.email == email, Teacher._password == _password)).first()

        elif '@mail.uic.edu.cn' in email: # Jaeger test
            result = Jaeger.query.filter(and_(Jaeger.email == email, Jaeger._password == _password)).first()
        else:
            return "invalid email"
        
        if result:
            print(result.name)
            print(result._password)
            return render_template('success.html',title='Success Login')
        else:
            return render_template('login.html',title='Sample Login',header='Sample Case')


@userBP.route('/luckyDraw',methods=['GET', 'POST'])
def luckyDraw():
    if request.method == 'GET':
        return render_template('luckyDrawConfig.html',title='Sample config',header='Sample ')
    else:
        NumOfF = int(request.form.get('numOfF'))
        NumOfS = int(request.form.get('numOfS'))
        NumOfT = int(request.form.get('numOfT'))
        luck = LuckyDrawer(100, NumOfF, NumOfS, NumOfT)
        result1 = luck.generateFirstWinner()
        result2 = luck.generateSecondWinner()
        result3 = luck.generateThirdWinner()
        return render_template('luckyDraw.html', title="results", title1=result1, title2=result2, title3=result3)
