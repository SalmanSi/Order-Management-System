from flask import Blueprint, render_template
from models import db

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/login')
def login():
    return "login page"

@auth_bp.route('/register')
def register():
    return "registration page"

@auth_bp.route('/logout')
def logout():
    return "logout page"
