import validators
from src.models import User


def register_validations(body):
    email: str = body['email']
    password: str = body['password']
    if not validators.email(email):
        return 'Invalid email'

    if User.query.filter_by(email=email).first():
        return 'Email already taken'

    if len(password) < 6:
        return "Password can't be lesser than 6 characters"
