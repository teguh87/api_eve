from schema.user import user 
from schema.category import category 
from schema.page import page
from schema.post import post 
from schema.media import media


SERVER_NAME = '127.0.0.1:5000'
SECRET_KEY = 'asaad2ewewe0ds.sds'

DOMAIN = {
    'user':user,
    'category':category,
    'page':page,
    'post':post,
    'media':media
}

#Mongo setup
MONGO_HOST = 'localhost'
MONGO_PORT = '27017'
#MONGO_USERNAME = 'root'
#MONGO_PASSWORD = 'root'
MONGO_DBNAME   = 'db'
IF_MATCH  = False


#Enable reads (GET), inserts (POST) and delete (DELETE) for resource collection
#If you omit this line, the API will default to ['GET'] and provide
#Read Only access to the endpoint
RESOURCE_METHODS = ['GET', 'POST']

#Enable reads (GET), edit (PATCH) or (PUT) and delete for item resource
#(default to read only-items access)
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

#Enable standard client cache directive for all resource exposed by the
#API. And Always override these global setting letter
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRED = 20
