from flask import Flask
from models import db,User
from auth import auth_bp
from routes import routes_bp
from flask_login import LoginManager

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///OMS.db"
app.config['SECRET_KEY'] = 'absdfjsdk'  # (load from env later on)

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')  # Optional: namespace routes
app.register_blueprint(routes_bp)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirect to login page if not logged in
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
