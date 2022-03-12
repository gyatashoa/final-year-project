import email
from src.database import db
from datetime import datetime
from src.database import User
from werkzeug.security import generate_password_hash


def save_user(body: dict):
    try:
        hashed_password = generate_password_hash(body['password'])
        dob = datetime.strptime(body['dob'], '%d %m %Y')
        user = User(
            email=body['email'],
            password=hashed_password,
            first_name=body['first_name'],
            last_name=body['last_name'],
            other_name=body.get('other_name', None),
            gender=body['gender'],
            dob=dob
        )
        db.session.add(user)
        db.session.commit()
        # db.session.commit()
    except Exception as e:
        return e
