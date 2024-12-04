from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route('/')
    def index():
        person = Person.query.all()
        return render_template('index.html', people = person)
    
    @app.route('/new_person')
    def new_person():
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')
        person = Person.query.all()

        return render_template('index.html', people = person)