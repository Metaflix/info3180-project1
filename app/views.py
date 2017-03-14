from app import app
from flask import render_template, request, redirect, url_for, jsonify, flash
from profileForm import profileForm
from flask.ext.sqlalchemy import SQLAlchemy
from app.User import User
from app import db
from datetime import datetime

db.create_all()


@app.route('/profile', methods=["GET", "POST"])
def addprofile():
    form = profileForm(request.form)

    if request.method == "POST":
        if form.validate():
            current_date = datetime.now().strftime("%a %d %b ")
            user = User(form.firstname.data, form.lastname.data,
                        form.age.data, form.sex.data, form.image.data, current_date, form.username.data)
            db.session.add(user)
            db.session.commit()

        return(render_template('profileForm.html', form=form))
    else:
        return render_template('profileForm.html', form=form)


@app.route('/profiles', methods=['GET', 'POST'])
def profiles():
    users = User.query.all()

    if request.headers.get('Content-Type') == 'application/json':
        user_dic = []
        for x in users:
            user_dic.append(
                {'id': x.id, 'age': x.age, 'sex': x.sex, 'image': x.image, 'username': x.username})
        return jsonify(users=user_dic)
    else:
        return render_template('profile.html', users=users)


@app.route('/profile/<int:userid>', methods=['GET', 'POST'])
def profileid(userid):
    users = User.query.filter_by(id=userid)
    if request.headers.get('Content-Type') == 'application/json':
        user_dic = []
        for x in users:
            user_dic.append(
                {'id': x.id, 'age': x.age, 'sex': x.sex, 'image': x.image, 'username': x.username})
            return jsonify(users=user_dic)
    else:
        return render_template('profile.html', users=users)
