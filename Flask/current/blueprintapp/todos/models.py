from blueprintapp.app import db

class Todo(db.Model):

    __tablename__ = 'todos'

    tid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    done = db.Coulmn(db.Boolean, nullable = False)

    