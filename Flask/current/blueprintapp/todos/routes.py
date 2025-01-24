from flask import redirect, request, render_template, url_for, Blueprint

from blueprintapp.app import db

from blueprintapp.todos.models import Todos

todos = Blueprint('todos', __name__ , template_folder='templates')

@todos.route('/')
def index():
    todos = Todos.query.all()
    return render_template('todos/index.html', todos = todos)

@todos.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('todos/create.html')
    
    elif request.method == 'POST':
        title = request.form.get('Title')
        description = request.form.get('Description')
        done = True if 'Done' in request.form.keys() else False

        description = description if description != '' else None

        todo = Todos(Title = title, Description= description, Done = done)


