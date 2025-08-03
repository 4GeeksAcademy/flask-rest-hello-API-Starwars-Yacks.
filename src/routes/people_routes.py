from flask import Blueprint, jsonify
from models import db, People

people_bp = Blueprint('people', __name__)

@people_bp.route('/people', methods=['GET'])
def get_all_people():
    people = People.query.all()
    return jsonify([p.serialize() for p in people]), 200

@people_bp.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
    if person:
        return jsonify(person.serialize()), 200
    return jsonify({"error": "Person not found"}), 404

