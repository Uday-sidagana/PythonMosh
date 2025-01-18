from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, render_template, url_for

db = SQLAlchemy

def create_app():
    app = Flask(__name__, template_folder='templates')
