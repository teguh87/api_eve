schema = {
        'name': {'type':'string', 'required':True},
        'label': {'type':'string'},
        'desc':{
                'type':'string',
                'minlength':1,
                'maxlength':200
            }
}


category = { 
        # set schema 
        'schema':schema,
        'resource_methods':['GET','POST'],
        'item_methods':['GET', 'PATCH', 'PUT', 'DELETE']
}
