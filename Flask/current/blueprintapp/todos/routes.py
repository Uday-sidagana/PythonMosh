from flask import redirect, request, render_template, url_for, Blueprint

from blueprintapp.app import db

from blueprintapp.todos.models import Todos

todos = Blueprint('todos', __name__ , template_folder='templates')

@todos.route()
def index():
    todos = Todos.query.all()
    return render_template('todos/index.html')