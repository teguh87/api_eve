from eve.auth import BasicAuth
from eve.auth import TokenAuth

class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        users = app.data.driver.db["user"]
        user = users.ind_one({"username": username})
        return user and  bcrypt.hashpw(password.encode('utf-8'), user['salt'].encode('utf-8')) == user['password']


class BaseTokenAuth(TokenAuth):
    def check_auth(self, token,  allowed_roles, resource, method):
        return True

