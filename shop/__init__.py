from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Setting the Flask Database Configuration 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shopswap.db'
db = SQLAlchemy(app)

# Setting DEBUG MODE 
app.config['DEBUG']=True

# Secret Key 
app.config['SECRET_KEY']='d8cb03689d01aba0c92249f8'

from shop import route


with app.app_context():
    db.create_all()