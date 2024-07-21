from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    favorites = db.relationship('Favorites', back_populates = "user")

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

    favorites = db.relationship('Favorites', back_populates = "planets")


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

    favorites = db.relationship('Favorites', back_populates = "people")


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


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user_username = db.Column(db.String(120), db.ForeignKey('user.username'))
    user = db.relationship(User, back_populates = 'favorites')

    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    # people_name = db.Column(db.String(120), db.ForeignKey('people.name'))
    people = db.relationship(People, back_populates = 'favorites')

    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # planets_name = db.Column(db.String(120), db.ForeignKey('planets.name'))
    planets = db.relationship(Planets, back_populates = 'favorites')


    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "User": self.user_id,
            # "Username": self.user_username,

            # "people name": self.people_name,
            "people id": self.people_id,

            # "planets name": self.planets_name,
            "planets id": self.planets_id
            # do not serialize the password, its a security breach
        }