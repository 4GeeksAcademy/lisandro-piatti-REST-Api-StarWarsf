"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# people1 = People (
#     name = "Luke Skywalker",
#     hair_color = "blond",
#     eye_color = "blue",
#     skin_color = "fair"   
# )
# db.session.add(people1)
# db.session.commit()

# people2 = People(
#     name = "C-3PO",
#     hair_color = "n/a", 
#     eye_color = "gold",
#     skin_color = "yellow"
# )
# db.session.add(people2)
# db.session.commit()

# people3 = People(
#     name = "R2-D2",
#     hair_color = "n/a",
#     eye_color = "red",
#     skin_color = "white, blue"
# )
# db.session.add(people3)
# db.session.commit()
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = list(map(lambda user : user.serialize(), users))
    return jsonify(users_list), 200

@app.route('/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return jsonify({ "info" : "Not Found"}), 404
    
    print(user)
    return jsonify(user.serialize()), 200

@app.route('/users', methods = ['POST'])
def create_user():
    user_body = request.get_json()
    user_db = User(
        username = user_body["username"],
        email = user_body["email"],
        password = user_body["password"],
        is_active = user_body["is_active"]
    )
    db.session.add(user_db)
    db.session.commit()
    return jsonify(user_db.serialize()), 201
    


'''
People Endpoints

'''

@app.route('/people', methods=['GET'])
def get_people_list():
    people_db = People.query.all()
    people_list = list(map(lambda people : people.serialize(), people_db))
    return jsonify(people_list), 200

@app.route('/people/<int:people_id>', methods = ['GET'])
def get_people(people_id):
    people = People.query.filter_by(id=people_id).first()
    if people is None:
        return jsonify({ "info" : "Not Found"}), 404
    return jsonify(people.serialize()), 200

'''
Planets Endpoints

'''

@app.route('/planets', methods=['GET'])
def get_planets_list():
    planets_db = Planets.query.all()
    planets_list = list(map(lambda planet : planet.serialize(), planets_db))
    return jsonify(planets_list), 200

@app.route('/planets/<int:planets_id>', methods = ['GET'])
def get_planets(planets_id):
    planet = Planets.query.filter_by(id=planets_id).first()
    if planet is None:
        return jsonify({ "info" : "Not Found"}), 404
    return jsonify(planet.serialize()), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
