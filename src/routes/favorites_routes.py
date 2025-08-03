from flask import Blueprint, jsonify
from models import db, Favorite, Planet, People

favorites_bp = Blueprint('favorites', __name__)

CURRENT_USER_ID = 1

@favorites_bp.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    favorites = Favorite.query.filter_by(user_id=CURRENT_USER_ID).all()
    return jsonify([f.serialize() for f in favorites]), 200

@favorites_bp.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    new_fav = Favorite(user_id=CURRENT_USER_ID, planet_id=planet_id)
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(new_fav.serialize()), 201

@favorites_bp.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    new_fav = Favorite(user_id=CURRENT_USER_ID, people_id=people_id)
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(new_fav.serialize()), 201

@favorites_bp.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    fav = Favorite.query.filter_by(user_id=CURRENT_USER_ID, planet_id=planet_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"msg": "Favorite planet deleted"}), 200
    return jsonify({"error": "Favorite not found"}), 404

@favorites_bp.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    fav = Favorite.query.filter_by(user_id=CURRENT_USER_ID, people_id=people_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"msg": "Favorite people deleted"}), 200
    return jsonify({"error": "Favorite not found"}), 404
