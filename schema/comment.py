schema = {
        'text':{
            'type':'string',
            'minlength':1,
            'maxlength':200
        },
        'author':{
            'type':'objectid',
            'data_relation':{
                'resource':'user',
                'field':'_id',
                'embeddable':True
            }
        }
}
