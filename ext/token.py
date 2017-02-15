from datetime import datetime, timedelta
from config.config import SECRET_KEY
import jwt

def create_token(user):
    #user = json.dumps(user, cls=JSONEncoder)

    payload ={
                # set user id
                'uid': str(user['_id']),
                # subject
                'sub': str(user['_id']),
                #issued at
                'iat': datetime.utcnow(),
                #expiry
                'exp': datetime.utcnow() + timedelta(days=1)
            }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token.decode('unicode_escape')

def parse_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return None

"""
try:
    import json
    from bson import ObjectId
except ImportError:
    pass


class JSONEncoder(json.JSONEncoder):
     def default(self, o):
         if isinstance(o, ObjectId):
              return str(o)
         return json.JSONEncoder.default(self, o)

"""
