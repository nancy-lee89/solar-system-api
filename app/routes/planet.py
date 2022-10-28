from flask import Blueprint, jsonify, request
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

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


# @planet_bp.route("", methods = ["GET"])
# def get_all_planets():
#     response = []
#     for planet in planets:
#         planet_dict = {
#             "id" : planet.id,
#             "name" : planet.name,
#             "description" : planet.description
#         }
#         response.append(planet_dict)
#     return jsonify(response),200

# @planet_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         response_string = f"Invalid planet_id: '{planet_id}' must be an integer"
#         return jsonify({"message": response_string}), 400

#     for planet in planets:
#         if planet.id == planet_id:
#             planet_dict = {
#                 "id" : planet.id,
#                 "name" : planet.name,
#                 "description" : planet.description
#             }
#             return jsonify(planet_dict), 200
#     response_message = f"Cound not find planet with ID {planet_id}"
#     return jsonify({"message": response_message}), 404