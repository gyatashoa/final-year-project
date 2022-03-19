from flask import Blueprint, jsonify, request
from src.constants import BASE_PREDICTION_URL
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.constants.http_codes import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

predictions = Blueprint("predictions", __name__,
                        url_prefix=BASE_PREDICTION_URL)


@predictions.get('predict')
@jwt_required()
def predict():
    user_id = get_jwt_identity()
    body: dict = request.json
    symptoms: list[str] = body.get('symptoms', [])
    if len(symptoms) is 0:
        return jsonify({'error': {'message': 'Invalid symptoms format'}}), HTTP_400_BAD_REQUEST

    return jsonify({}), HTTP_201_CREATED
