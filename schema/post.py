schema = {
    'slug':{'type':'string', 'required':True},
    'title':{
        'type':'string',
        'required':True,
        'minlength':1,
        'maxlength':50
    },
    'text':{
        'type':'string'
    },
    'page':{
        'type':'objectid',
        'data_relation':{
            'resource':'page',
            'field':'_id',
            'embeddable':True
        }
    },
    'author':{
        'type':'objectid',
        'data_relation':{
            'resource':'user',
            'field':'_id',
            'embeddable':True
        }
    },
    'media':{
        'type':'list',
        'schema':{
            'data_relation':{
                'resource':'media',
                'field':'_id',
                'embeddable':True
            }
        }
    }
}

post = {
    'schema':schema,
    'resource_methods':['GET', 'POST'],
    'item_methods':['GET', 'PATCH', 'PUT', 'DELETE']
}
