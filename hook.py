import bcrypt
from app import app 
from flask import json, request, Response
from flask.ext.api import status
from ext.token import create_token

@app.route('/auth', methods=['POST'])
def auth():
    # init all value
    response = None
    app.logger.info('initialize loggin request')
    # Retrive Json body post method
    req = request.get_json()
    app.logger.debug('paylod %s'%(req))
    # Retrive all user meta 
    users = app.data.driver.db['user']
    user = users.find_one({"username": req["username"]})
    if user:
        # Check password change password to hasing 
        isPass = bcrypt.hashpw(req["password"].encode('utf-8'),user["salt"].encode('utf-8')) == user['password']
        if isPass:
            response = json.jsonify({"token" :create_token(user)}), status.HTTP_302_FOUND
        else:
            response = json.jsonify({"_status" :"ERR", "_error":
                {"message":"Authorities failed please check your cridential!", "code": 400}}), status.HTTP_400_BAD_REQUEST
    else:
        response = json.jsonify({"_status" :True, "_error":
            {"message":"Can't find any user with username %s please check your cridential!"
            %(req['username']), "code": 400}}),status.HTTP_400_BAD_REQUEST
    return response
