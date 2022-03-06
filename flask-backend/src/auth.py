from flask import Blueprint, jsonify, request
from .constants import BASE_AUTH_URL


auth = Blueprint("auth", __name__, url_prefix=BASE_AUTH_URL)


@auth.post('register')
def register():
    # request.gejson().
    return jsonify({"message": "Register"}), 201
