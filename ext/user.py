import bcrypt


def before_save_user(documents):
    for document in documents:
        document['salt'] = bcrypt.gensalt().encode('utf-8')
        password = document['password'].encode('utf-8')
        document['password'] = bcrypt.hashpw(password, document['salt'])
