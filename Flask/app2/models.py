from flask_login import UserMixin
from app import db 

class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable = False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"Name = {self.name}, age = {self.age}, Job = {self.job}"

class User(db.Model, UserMixin ):

    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable =False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f"user: {self.name}"

    def get_id(self):
        return self.uid
    

    
