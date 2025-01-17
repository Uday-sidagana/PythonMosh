from flask import render_template, request, redirect, url_for
from models import Person
from models import User
from flask_login import login_user, logout_user, current_user, login_required




def register_routes(app, db, bcrypt):

    @app.route('/login/', methods = ['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return redirect(url_for('index'))
        
        elif request.method == 'POST':
            Uid = request.form.get('uid')
            Name = request.form.get('name')
            Password = request.form.get('password')
            
            user = User.query.filter(User.name == Name).first()

            if user:
                if bcrypt.check_password_hash(user.password, Password):
                    login_user(user)
                
                    return render_template('index.html') #,current_user = user.name) #,people = person)
                

                
                # if user:
                    
                #     # person = Person.query.all()
                #     login_user(user)
                
                #     return render_template('index.html', current_user = user.name) #,people = person)
                
                else:
                    return "Wrong Password"
            
            else:
                return "No User Found"
        

    @app.route('/logout/', methods = ['GET'])

    def logout():
        if request.method == 'GET':
            logout_user()
            person = Person.query.all()
            return render_template('index.html', people = person )
        # elif request.method == 'POST':

    @app.route('/signup/', methods = ['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        

        elif request.method == 'POST':
            Uid = request.form.get('uid')
            Name = request.form.get('name')
            Password = request.form.get('password')
            Role = request.form.get('role')
            Description = request.form.get('description')
            hashed_password = bcrypt.generate_password_hash(Password)

            user = User(uid = Uid, name = Name, password = hashed_password, role=Role, description=Description)
            db.session.add(user)
            db.session.commit()


    

            return render_template('login.html')
        
    @app.route('/loginbttn/', methods=['POST'])
    def loginbttn():
        Uid = request.form.get('uid')
        return render_template('login.html', uid = Uid)
    
    @app.route('/signupbttn/', methods = ['GET'])
    def signupbttn():
        return render_template('signup.html')



    @app.route('/index/', methods =['GET', 'POST'])
    
    def index():
        if request.method == 'GET':
            person = Person.query.all()
            # user = User.query.all()
            return render_template('index.html', people = person, current_user= current_user )
        
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
    