from flask import Blueprint, render_template
from models import db

auth_bp=Blueprint('auth',__name__,template_folder='templates')

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    return "logout page"
