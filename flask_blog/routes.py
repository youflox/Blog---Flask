from flask import render_template, url_for, flash, redirect
from flask_blog import app, db, bcrypt
from flask_blog.models import User, Post
from flask_blog.forms import *

posts = [
    {
        'author': 'Nanda',
        'title' : 'Blog post',
        'content' : 'Lorem ipsum dolor sit amet, '
                    'consectetur adipiscing elit, sed do eiusmod tempor '
                    'incididunt ut labore et dolore magna aliqua. Ut enim ad minim '
                    'veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip '
                    'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                    'voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
                    'Excepteuroccaecat cupidatat non proident, sunt in culpa qui officia deserunt'
                    ' mollit anim id est laborum.',
    },
    {
      'author' : 'Ratna',
        'title' : 'Blog post',
        'content' : 'Lorem solus specter zoom pamatne.'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Account Created!!')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form )

@app.route('/login', methods = ['POST','GET'])
def login():
     form = LoginForm()
     return render_template('login.html', title = 'Login', form=form )
