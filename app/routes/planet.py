from flask import Blueprint, jsonify, request, abort, make_response
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

def get_one_planet_or_abort(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response_str = f"Invalid planet_id '{planet_id}'. ID must be an integer"
        abort(make_response(jsonify({"message": response_str}),400))

    matching_planet = Planet.query.get(planet_id)

    if matching_planet is None:
        response_str = f"Planet with id '{planet_id}' was not found in the database."
        abort(make_response(jsonify({"message": response_str}),404))
    return matching_planet

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        size = request_body["size"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planet_bp.route("", methods = ["GET"])
def get_all_planets():
    
    name_param = request.args.get("name")
    if name_param is None:
        planets = Planet.query.all()
    else:
        planets = Planet.query.filter_by(name=name_param)
    
    response = []
    for planet in planets:
        planet_dict = {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description,
            "size": planet.size
        }
        response.append(planet_dict)
    return jsonify(response),200

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    chosen_planet = get_one_planet_or_abort(planet_id) 

    planet_dict = {
    "id" : chosen_planet.id,
    "name" : chosen_planet.name,
    "description" : chosen_planet.description,
    "size": chosen_planet.size
    }
    return jsonify(planet_dict), 200

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet_with_new_vals(planet_id):

    chosen_planet = get_one_planet_or_abort(planet_id)

    request_body = request.get_json()

    if "name" not in request_body or\
    "description" not in request_body  or \
    "size" not in request_body:
        return jsonify({"message": "Request must include name, description and size"}, 404)

    chosen_planet.name = request_body["name"]
    chosen_planet.description = request_body["description"]
    chosen_planet.size = request_body["size"]

    db.session.commit()

    return jsonify({"message": f"Successfully replaced planet with id '{planet_id}'"}), 200
    
@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    chosen_planet = get_one_planet_or_abort(planet_id)
    db.session.delete(chosen_planet)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted planet with id '{planet_id}'"}), 200