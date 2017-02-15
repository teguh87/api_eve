schema = {
        'name':{'type':'string', 'required':True},
        'category':{
            'type':'objectid',
            'data_relation':{
                'field':'_id',
                'resource':'category',
                'embeddable':True
            }
        },
        'template_url':{'type':'string', 'required':True},
        'label':{'type':'string', 'required':True}
}

page = {
    'schema':schema,
    'resource_methods':['GET', 'POST'],
    'item_methods':['GET', 'PATCH', 'PUT', 'DELETE']
}
