from flask import render_template, request, redirect, url_for
from models import Person
from models import User
from flask_login import login_user, logout_user, current_user, login_required




def register_routes(app, db, bcrypt):

    @app.route('/login/<uid>', methods = ['GET', 'POST'])
    def login(uid):
        user = User.query.get(uid)
        login_user(user)
    
        return render_template('index.html', current_user = user.name)
    @app.route('/logout/', methods = ['GET'])
    def logout():
        logout_user()
        return "success"


    @app.route('/index/', methods =['GET', 'POST'])
    def index():
        if request.method == 'GET':
            person = Person.query.all()
            user = User.query.all()
            return render_template('index.html', people = person, current_user= user )
        
        elif request.method == 'POST':
            Name = request.form.get('name')
            Age = request.form.get('age')
            Job = request.form.get('job')

            # return f"{Name} {Age} {Job}"

            person = Person(name=Name, age=Age, job=Job)
            db.session.add(person)
            db.session.commit()


            return redirect(url_for('index'))
    
    @app.route('/delete/<int:pid>', methods = ['DELETE'])
    def delete(pid):

        Person.query.filter(Person.pid == pid).delete()


        db.session.commit()
        people = Person.query.all()
        return render_template('index.html', people = people)
    
    @app.route('/details/<pid>')
    def details(pid):

        person = Person.query.filter(Person.pid == pid).first()

        return render_template('detail.html', person = person)
    