from flask import Blueprint, jsonify, request
from .services.validators import register_validations
from src.constants.http_codes import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .constants import BASE_AUTH_URL


auth = Blueprint("auth", __name__, url_prefix=BASE_AUTH_URL)


@auth.post('register')
def register():
    msg = register_validations(request.json)
    if msg is not None:
        return jsonify({
            'error': {
                'message': msg,
            }
        }), HTTP_400_BAD_REQUEST
    return jsonify({"message": "Register"}), HTTP_201_CREATED
