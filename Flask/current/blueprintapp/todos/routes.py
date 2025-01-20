from flask import redirect, request, render_template, url_for, Blueprint

from blueprintapp.app import db

from blueprintapp.blueprints.todos.models import Todos

todos = Blueprint('todos',__name__, template_folder='templates')