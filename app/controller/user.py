from flask import Blueprint,render_template, request, jsonify
from app.models.base import db
from app.models.teacher import users
from sqlalchemy import or_,and_,all_,any_

userBP = Blueprint('user',__name__)

@userBP.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',title='Sample Login',header='Sample Case')
    else:

        email = request.form.get('email')
        _password = request.form.get('password')

        print(email, _password)


        if '@uic.edu.hk' in email:
            result = users.query.filter(and_(users.email == email,users._password == _password)).first()
        else:
            return "invalid email"
        
        if result:
            print(result.name)
            print(result._password)
            return render_template('success.html',title='Success Login')
        else:
            return render_template('login.html',title='Sample Login',header='Sample Case')

