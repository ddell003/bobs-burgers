class User:

    fields = [
        'first_name',
        'last_name',
        'email',
        'deleted'
    ]

    soft_delete = True

    def __init__(self):

        for field in self.fields:
            setattr(self, field, None)


    def __repr__(self):

        return repr('User')


