from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

# Setting the Flask Database Configuration 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shopswap.db'
db = SQLAlchemy(app)

# Initialising Bcrypt 
bcrypt=Bcrypt(app)

# Initializing login manager for Login page 
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category='info'

# Setting DEBUG MODE 
app.config['DEBUG']=True

# Secret Key 
app.config['SECRET_KEY']='d8cb03689d01aba0c92249f8'

from shop import route


with app.app_context():
    db.create_all()