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

    def __init__(self, first_name=None, last_name=None, email=None, deleted=0):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.deleted = deleted

    def __repr__(self):

        return '<User %r>' % (self.first_name)




