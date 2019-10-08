from model import Model


class MenuSection(Model):
    """
    Each database table should have a model instances that extends the base model for core database functionality
    The majority of the magic happens in the base
    """
    # define the fields the table has
    fields = [
        'name',
        'deleted'
    ]

    # declare the name of the table
    table = 'menu_sections'

    defaults = [
        'Burgers',
        'Sides',
        'Desserts',
        'Drinks',
        'Beers',
        'Wines'
    ]
