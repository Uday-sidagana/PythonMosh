from flask import render_template, request
from models import Person


def register_routes(app, db):

    @app.route('/', methods =['GET', 'POST'])
    def index():
        if request.method == 'GET':
            person = Person.query.all()
            return render_template('index.html', people = person)
        
        elif request.method == 'POST':
            Name = request.form.get('name')
            Age = request.form.get('age')
            Job = request.form.get('job')

            # return f"{Name} {Age} {Job}"

            person = Person(name=Name, age=Age, job=Job)
            db.session.add(person)
            db.session.commit()


            person = Person.query.all()
            return render_template('index.html', people = person)
    
    @app.route('/delete/<pid>', methods = ['DELETE'])
    def delete(pid):

        Person.query.filter(Person.pid == pid).delete()


        db.session.commit()
        people = Person.query.all()
        return render_template('index.html', people = Person)
    