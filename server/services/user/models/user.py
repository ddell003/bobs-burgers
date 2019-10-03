from model import Model


class User(Model):
    """
    Each database table should have a model instances that extends the base model for core database functionality
    The majority of the magic happens in the base
    """
    # define the fields the table has
    fields = [
        'first_name',
        'last_name',
        'email',
        'deleted'
    ]
    # declare the name of the table
    table = 'users'

    def __init__(self):

        # lets set the fields on init
        for field in self.fields:
            setattr(self, field, None)

    def __repr__(self):

        return repr('User')




