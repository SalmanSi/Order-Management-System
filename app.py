from flask import Flask
from models import db
from auth import auth_bp
from routes import routes_bp

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///OMS.db"
app.config['SECRET_KEY'] = 'absdfjsdk'  # Prefer loading from .env file for security

# Initialize database
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')  # Optional: namespace routes
app.register_blueprint(routes_bp)

# Create database tables (optional for dev only)
# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
