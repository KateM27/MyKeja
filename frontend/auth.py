from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import LandLord
from . import db
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method ==  'POST':
        email = request.form.get('email')
        Firstname = request.form.get('firstName')
        surname = request.form.get('secondName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(Firstname) < 2:
             flash('first name must be greeter than 1 characters', category='error')
        elif len(surname) < 2:
             flash('second name must be greeter than 1 characters', category='error')
        elif len(email) < 4:
            flash('email must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 7:
            flash('password must be 8 characters', category='error')
        else:
            user = LandLord (email = email, First_name =  Firstname, second_name = surname, password = generate_password_hash(password1, method='sha256'))
            db.session.add(user)
            db.session.commit()
            flash('account created', category='success')
            return redirect(url_for('views.lordview'))

    return render_template('signup.html')

    
""" @auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.method == 'POST':
          email = request.form['email']
          password = request.form['password']


          #retrieve from data base.
        if email in user_accounts and user_accounts[email] == password:
            return redirect(url_for('apartments'))
        else:
            print ('Invalid Login. Please try again.')
            return redirect(url_for("login"))

    return render_template("login.html", boolean=True) """

@auth.route('/logout')
def logout():
    """ return redirect(url_for("dashboard")) """
    return render_template('signup.html')

