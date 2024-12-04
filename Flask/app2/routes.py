from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route('/')
    def index():
        person = Person.query.all()
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')
        return render_template('index.html', people = person)
    
    