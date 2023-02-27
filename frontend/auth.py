from flask import Blueprint, render_template, request, flash, redirect, url_for
from mykeja import db, User
from .models import LandLord
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user 

auth = Blueprint('auth', __name__)


# Tenant information
tenants = {}

# Caretaker information
caretakers = {}

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     data = request.form
#     print(data)
#     return render_template('login.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = LandLord.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.lordview'))
            else:
                flash('incorrect password, try again.', category='error')
        else:
            flash('email does not exist.', category="error")

    return render_template('login.html', boolean=True)


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method ==  'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        surname = request.form.get('secondName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        u = User(email=email, firstname=firstname, surname=surname, password=password1)
        db.session.add(u)
        db.session.commit()

        if len(firstname) < 2:
             flash('first name must be greater than 1 characters', category='error')
        elif len(surname) < 2:
             flash('second name must be greater than 1 characters', category='error')
        elif len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif password1 != password2:
             flash('passwords don\'t match', category='error')

        user = LandLord.query.filter_by(email=email).first()

        if len(firstname) < 2:
             flash('first name must be greeter than 1 characters', category='error')
        elif len(surname) < 2:
             flash('second name must be greeter than 1 characters', category='error')
        elif user:
            flash('email already exists')
        elif len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 7:
            flash('password must be 8 characters', category='error')
        else:
            user = LandLord (email = email, first_name =  firstname, second_name = surname, password = generate_password_hash(password1, method='sha256'))
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('account created', category='success')
            return redirect(url_for('views.lordview'))

    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

