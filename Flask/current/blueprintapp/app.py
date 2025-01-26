from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, render_template, url_for

db = SQLAlchemy

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'

    db.init_app(app)


    #import and register all blueprints

    from blueprintapp.todos.routes import todos
    app.register_blueprint(todos)

    migrate = Migrate(app, db)

    return app

