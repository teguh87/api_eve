schema = { 'name':{'type':'string', 'required':True},
        'size':{'type':'integer'},
        'link':{'type':'string'}
        
}


media = {
    'schema':schema,
    'resource_methods':['GET', 'POST'],
    'item_methods':['GET', 'PATCH', 'PUT']
}
