from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shopswap.db'
db = SQLAlchemy(app)

# Setting DEBUG MODE 
app.config['DEBUG']=True


from shop import route

with app.app_context():
    db.create_all()