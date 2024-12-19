import jwt
import datetime

SECRET_KEY = 'your_secret_key'

def generate_token(member_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'id': member_id, 'exp': expiration_time}, SECRET_KEY, algorithm='HS256')
    return token

def authenticate(token):
    if not token:
        return False
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end]
