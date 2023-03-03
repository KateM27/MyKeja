from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user 


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")
    
@views.route('/dashboard')
@login_required
def lordview():
    return render_template("landlordview.html")

@views.route('/new_apartment')
@login_required
def new_house():
    return render_template("landlord.html")
