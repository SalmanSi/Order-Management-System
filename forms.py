from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class OrderForm(FlaskForm):
    order_id = StringField('Order ID', validators=[DataRequired()])
    num_items = IntegerField('Number of Items', validators=[DataRequired()])
    delivery_date = DateField('Delivery Date', validators=[DataRequired()])
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    recipient_name = StringField('Recipient Name', validators=[DataRequired()])
    recipient_address = StringField('Recipient Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditOrderForm(FlaskForm):
    # No order_id field - it cannot be changed
    num_items = IntegerField('Number of Items', validators=[DataRequired()])
    delivery_date = DateField('Delivery Date', validators=[DataRequired()])
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    recipient_name = StringField('Recipient Name', validators=[DataRequired()])
    recipient_address = StringField('Recipient Address', validators=[DataRequired()])
    submit = SubmitField('Update')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')