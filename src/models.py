from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)


    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)


    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color
            # do not serialize the password, its a security breach
        }
    


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(120), unique=False, nullable=False)
    manufacturer = db.Column(db.String(120), unique=False, nullable=False)
    passengers = db.Column(db.Integer, unique=False, nullable=False)
    length = db.Column(db.Float, unique=False, nullable=False)


    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "passengers": self.passengers,
            "length": self.length
            # do not serialize the password, its a security breach
        }
