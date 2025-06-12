from flask import Flask
from models import db
from auth import auth_bp
from routes import routes_bp

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///OMS.db"
app.config['SECRET_KEY']='absdfjsdk' # load from env file later

db.init_app(app)

# Register all blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)
