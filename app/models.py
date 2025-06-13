from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    completed = db.Column(db.Boolean)

    def __repr__(self):
        return self.text