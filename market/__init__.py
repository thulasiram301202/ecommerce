from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '641b39ed0ccf8094ed5eee6a'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  
login_manager = LoginManager(app)  
login_manager.login_view = 'login_page'  

migrate = Migrate(app, db)  

from market import routes  
from market.model import User  
