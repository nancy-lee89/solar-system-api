from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

planets = [Planet(1, "Mercury", "the smallest planet in the Solar System"),
            Planet(2, "Venus", "The second planet from the sun"),
            Planet(3, "Earth", "The third planet from the sun")
]

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

@planet_bp.route("", methods = ["GET"])
def get_all_planets():
    response = []
    for planet in planets:
        planets_dict = {
            "id" : planet.id,
            "name" : planet.name,
            "description" : planet.description
        }
        response.append(planets_dict)
    return jsonify(response),200