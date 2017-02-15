schema = {
    'username': {'type': 'string', 'required': True, 'unique': True},
    'password': {'type': 'string'},
    'salt':{'type':'string'}
}

user ={

    # the standard account entry point is defined as
    # '/user/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/user/<username>'.

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username',
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,
    # Finally, let's add the schema definition for this endpoint.
    'schema': schema,
    'resource_methods': ['GET','POST'],
    'item_methods': ['GET','PATCH', 'PUT', 'DELETE'],
}

