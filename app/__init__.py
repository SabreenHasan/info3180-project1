from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = "r@ndomk3y"
UPLOAD_FOLDER = "./app/static/uploads"

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:@localhost/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # hide warning

db = SQLAlchemy(app)

manage_login = LoginManager()
manage_login.init_app(app)
manage_login.login_view = 'login'

app.config.from_object(__name__)
filefolder = app.config['UPLOAD_FOLDER']
app.debug= True
from app import views