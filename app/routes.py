# app/routes.py
from flask import render_template
from app import app, db
from app.models import User, Post

@app.route('/')
def home():
    # new_user = User(username='ali', email='ali@gmail.com')
    # db.session.add(new_user)
    # db.session.commit()
    users = User.query.all()
    posts = Post.query.all()
    return render_template('home.html', users=users, posts=posts)
