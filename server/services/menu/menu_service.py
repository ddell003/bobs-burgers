from services.menu.models.menu_section import MenuSection
from services.menu.models.menu_item import MenuItem


class MenuService:
    """

    """
    def get_menu_sections(self):
        """

        :return:
        """
        return self.section_builder().get()

    def section_builder(self):
        return MenuSection()

    def item_builder(self):
        return MenuItem()

    def get_section(self, section_id):
        """
        Lets get a particular section
        :param user_id:
        :return:
        """

        return self.section_builder().get_by_id(section_id)

    def get_menu_items(self):
        """
        Lets get a list of all items and return it
        :return: 
        """""
        return self.item_builder().get()

    def get_item(self, id):
        """
        Lets get a particular item
        :param id:
        :return:
        """
        return self.item_builder().get_by_id(id)

    def set_up_sections(self):
        """
        Lets set up the menu section table and load in some default users .. should move this to a factory
        :return:
        """
        menu_section = MenuSection()
         # define sql to create users table
        table_query = """
        CREATE TABLE IF NOT EXISTS menu_sections (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            deleted INTEGER DEFAULT 0
        )
        """
        # lets connect to db through the model
        conn = menu_section.get_connection()
        cur = conn.cursor()
        # lets run the query we made
        cur.execute(table_query)

        # lets truncate the table so we always start out with 5 users
        cur.execute('DELETE from menu_sections;')

        # see if any users exist and grab their emails
        existing_items = cur.execute('SELECT * FROM menu_sections;').fetchall()
        made_items = {item for item in existing_items}

        # loop over default users and create them
        for item in menu_section.defaults:

            # lets not recreate existing users in db
            if item in made_items:
                continue
            create = """
            INSERT INTO menu_sections (name)
            VALUES 
            """

            # create db entry for current user
            create += "('{}')".format(item)
            cur.execute(create)

        # lets save the changes to the db
        conn.commit()
        """

        :return:
        """
        return self.section_builder().get()
    def set_up_items(self):
        """
        Lets set up the menu items table and load in some default users .. should move this to a factory
        :return:
        """
        menu_item = MenuItem()
        # define sql to create users table
        table_query = """
        CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL,
        section_id INTEGER NOT NULL,
        deleted INTEGER DEFAULT 0
        )
        """

        # lets connect to db through the model
        conn = menu_item.get_connection()
        cur = conn.cursor()
        # lets run the query we made
        cur.execute(table_query)

        # lets truncate the table so we always start out with 5 users
        cur.execute('DELETE from menu_items;')

        # see if any users exist and grab their emails
        existing_items = cur.execute('SELECT * FROM menu_items;').fetchall()
        made_items = {item['name'] for item in existing_items}

        # loop over default users and create them
        for item in menu_item.defaults:

            # lets not recreate existing users in db
            if item['name'] in made_items:
                continue
            create = """
            INSERT INTO menu_items (`name`, `description`, `price`, `section_id`)
            VALUES 
            """
    
            # create db entry for current user
            create += " ('{}', '{}', '{}', '{}')".format(item['name'], item['description'], item['price'],  item['section_id'])

            cur.execute(create)

        # lets save the changes to the db
        conn.commit()
