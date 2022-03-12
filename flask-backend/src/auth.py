from flask import Blueprint, jsonify, request
from .services.validators import register_validations
from .services.auth_services import save_user
from src.constants.http_codes import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .constants import BASE_AUTH_URL


auth = Blueprint("auth", __name__, url_prefix=BASE_AUTH_URL)


@auth.post('register/')
@auth.post('register')
def register():
    msg = register_validations(request.json)
    if msg is not None:
        return jsonify({
            'error': {
                'message': msg,
            }
        }), HTTP_400_BAD_REQUEST
    res = save_user(request.json)
    if res is None:
        return jsonify({"message": "user created",
                        "user": {
                            "email": request.json['email']
                        }}), HTTP_201_CREATED
    return jsonify({"error": {
        "message": "Something went wrong on the server, please try again later"
    }}), HTTP_400_BAD_REQUEST
