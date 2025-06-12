from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)
    logs = db.relationship('Log', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(20), unique=True, nullable=False)
    num_items = db.Column(db.Integer, nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    sender_name = db.Column(db.String(100), nullable=False)
    recipient_name = db.Column(db.String(100), nullable=False)
    recipient_address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default="Ongoing")

    # Foreign key to link the user who created the order
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Relationship to logs
    logs = db.relationship('Log', backref='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.order_id}>'

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign keys to link to user and order
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def __repr__(self):
        return f'<Log {self.action} on Order {self.order_id} by User {self.user_id}>'
