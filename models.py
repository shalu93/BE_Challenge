from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    place = db.Column(db.String(150))
    email = db.Column(db.String(100))

    def __init__(self, name, place, email):
        self.name = name
        self.place = place
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'place': self.place,
            'email':self.email
        }