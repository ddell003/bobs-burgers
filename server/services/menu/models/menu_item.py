from model import Model


class MenuItem(Model):
    """
    Each database table should have a model instances that extends the base model for core database functionality
    The majority of the magic happens in the base
    """
    # define the fields the table has
    fields = [
        'name',
        'description',
        'price',
        'section_id',
        'deleted'
    ]

    # declare the name of the table
    table = 'menu_items'

    defaults = [
        {
            'name':'"New Bacon-ings" - Comes with Bacon',
            'description':'Bacon Burger',
            'price':'5.95',
            'section_id':'1'

        },
        {
            'name':'Foot Feta-ish Burger',
            'description':'Comes with feta cheese.',
            'price':'5.95',
            'section_id':'1'

        },
        {
            'name':'Mission A-Corn-Plished Burger',
            'description':'Comes with Corn Salsa',
            'price':'5.95',
            'section_id':'1'

        },
        {
            'name':'Hit Me With Your Best Shallot Burger',
            'description':'Classic burger but better',
            'price':'5.95',
            'section_id':'1'

        },
        {
            'name':"Somethings NOT Fishy Burger - (100% Beef)",
            'description':'Not served with fish',
            'price':'5.95',
            'section_id':'1'

        },
        {
            'name':"Fries",
            'description':'Fries and moe fries',
            'price':'1.95',
            'section_id':'2'

        },
        {
            'name':"Orange Fries",
            'description':'Fries from the orange potato',
            'price':'1.95',
            'section_id':'2'

        },
        {
            'name':"Salad",
            'description':'Not fries',
            'price':'1.95',
            'section_id':'2'

        },
        {
            'name':"Cake By the Ocean",
            'description':'Cake of course',
            'price':'3.95',
            'section_id':'3'

        },
        {
            'name':"Cookies By the Seashore",
            'description':'Cookie skillet served with milk',
            'price':'3.95',
            'section_id':'2'

        },
        {
            'name':"Fizz",
            'description':'Soda as some people call it',
            'price':'.95',
            'section_id':'4'

        },
        {
            'name':"Coffee",
            'description':'French pressed',
            'price':'.95',
            'section_id':'4'

        },
         {
            'name':"House Red",
            'description':'Imported from next door',
            'price':'4.95',
            'section_id':'6'

        },
        {
            'name':"House Not Red",
            'description':'Imported from next door',
            'price':'4.95',
            'section_id':'6'

        },
        {
            'name':"On Draft",
            'description':'Beers on draft may vary',
            'price':'3.95',
            'section_id':'5'

        },
         {
            'name':"Imports",
            'description':'Beer',
            'price':'4.95',
            'section_id':'5'

        },
    ]

