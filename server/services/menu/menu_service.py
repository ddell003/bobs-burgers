from services.menu.models.menu_section import MenuSection


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

    def get_section(self, section_id):
        """
        Lets get a particular section
        :param user_id:
        :return:
        """

        return self.section_builder().get_by_id(section_id)


    def set_up_sections(self):
        """
        Lets set up the users table and load in some default users .. should move this to a factory
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
