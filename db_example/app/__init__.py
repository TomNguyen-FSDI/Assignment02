#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Simple app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import render_template
from flask import url_for, redirect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


# from app import routes
from app.database import *
from app import db, User


@app.route('/')
@app.route('/home')
@app.route('/index.html')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/create', methods=['POST'])
def create():
    input = request.form
    first_name = input['first_name']
    last_name = input['last_name']
    hobbies = input['hobbies']
    create_my_user(first_name, last_name, hobbies)
    return redirect(url_for('users'))


@app.route('/delete', methods=['POST'])
def delete():
    input = request.form
    try:
        user_id = int(input['id'])
    except ValueError:
        print("ValueError not an integer")
    else:
        print("input from user is: {}".format(user_id))
        ans = User.query.filter_by(id = user_id).first()
        if ans is not None:
            db.session.delete(ans)
            db.session.commit()
    return redirect(url_for('users'))


@app.route('/read', methods=['GET'])
def read():
    input = request.args.get('id')
    try:
        user_id = int(input)
    except ValueError:
        print("ValueError not an integer")
    else:
        print("input from user is: {}".format(user_id))
        ans = User.query.filter_by(id = user_id).first()
        if ans is not None:
            return redirect('/users/{}'.format(user_id))
            # return redirect( url_for('users',uid=4))
            # {{ url_for ('about',uid=1) }}
    return redirect(url_for('users'))


@app.route('/update', methods=['POST'])
def update():
    input = request.form
    try:
        user_id = int(input['id'])
    except ValueError:
        print("ValueError not an integer")
    else:
        first_name = input['first_name']
        last_name = input['last_name']
        hobbies = input['hobbies']
        # if first_name is empty no change
        ans = User.query.filter_by(id = user_id).first()
        if (ans is not None):
            if first_name != '':
                ans.first_name = first_name
            if last_name != '':
                ans.last_name = last_name
            if hobbies != '':
                ans.hobbies = hobbies
            db.session.commit()
    return redirect(url_for('users'))


@app.route('/users')
def users():
    user = User.query.all()
    return render_template("users.html", user = user)


@app.route("/users/<int:uid>")
def about(uid):
    user = User.query.filter_by(id = uid).first()
    # return me = {
    #     "first_name" : user.first_name,
    #     "last_name" : user.last_name,
    #     "hobbies" : user.hobbies
    # }
    return render_template("about.html", user = user)


@app.route("/users/all")
def all():
    user = User.query.all()
    # data = ''
    # for next_user in user:
    #     data = data + "{} {} {}<br>".format(next_user.first_name, next_user.last_name, next_user.hobbies)
    # return data
    return render_template("users_all.html", user = user)


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is <br>%s</p>" % user_agent


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", names=name)


def create_my_user(first_name, last_name, hobbies):
    """Simple user creation function"""
    db.session.add(
        User(
            first_name = first_name,
            last_name = last_name,
            hobbies = hobbies
        )
    )
    db.session.commit()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
