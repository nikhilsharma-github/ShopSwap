# Importing flask form library
from flask_wtf import FlaskForm
# importing input datatyping from the library
from wtforms import StringField, PasswordField, SubmitField

# Validation of Input Fields 
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

# Importing User Object from models.py 
from shop.models import User



class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
        
    def validate_email_address(self,email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
        
    username =  StringField(label='',validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='',validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
    username = StringField(label='',validators=[DataRequired()])
    password = PasswordField(label='',validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')

