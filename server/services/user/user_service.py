from services.user.models.user import User


class UserService:
    """
    Using a Service Repository Pattern
    Service is where all the business logic takes place - what do we want to do with the user data
    Repository sites on top of a database - file or array
    Model represents a database entity - the user
    """

    default_list = [
            {
                'id':'1',
                'first_name':'Bob',
                'last_name':'Belcher',
                'email':'bob@bobsburgers.gmail.com',
                'deleted': 0
            },
            {
                'id':'2',
                'first_name':'Linda',
                'last_name':'Belcher',
                'email':'linda@bobsburgers.gmail.com',
                'deleted': 0
            },
            {
                'id':'3',
                'first_name':'Tina',
                'last_name':'Belcher',
                'email':'linda@bobsburgers.gmail.com',
                'deleted': 0
            },
            {
                'id':'4',
                'first_name':'Gene',
                'last_name':'Belcher',
                'email':'linda@bobsburgers.gmail.com',
                'deleted': 0
            },
            {
                'id':'5',
                'first_name':'Louise',
                'last_name':'Belcher',
                'email':'linda@bobsburgers.gmail.com',
                'deleted': 0
            },
        ]
    def builder(self):
        return User()

    def get_default_users(self):
        return self.default_list

    def get_users(self):
        """
        Lets get the list of users
        :return:
        """
        return self.builder().get()


    def get_user(self, user_id):
        """
        Lets get a particular user
        :param user_id:
        :return:
        """

        return self.builder().get_by_id(user_id)

    def create_user(self, request_validator):
        """
        Lets create the user
        :param request_validator:
        :return:
        """
        user = User()
        request_validator.validate_fields(user)

        data = request_validator.request.json
        return user.create(data)

    def update_user(self, request_validator, user):

        """
        Lets update the user
        :param request_validator:
        :param user:
        :return:
        """

        # validate the data using user model
        user_model = User()
        request_validator.validate_fields(user_model)

        print(user)

        # get the input data from the request
        user_data = request_validator.request.json
        # we only want to update certain fields
        user['first_name'] = user_data['first_name']
        user['last_name'] = user_data['last_name']
        user['email'] = user_data['email']

        return user_model.update(user['id'], user)

    def delete_user(self, user):
        """
        Lets mark this user as deleted
        :param user:
        :return:
        """

        user_model = User()
        user_model.delete(user['id'])

    def set_up_users(self):
        """
        Lets set up the users table and load in some default users .. should move this to a factory
        :return:
        """
        user = User()
         # define sql to create users table
        user_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            deleted INTEGER DEFAULT 0
        )
        """
        # lets connect to db through the model
        conn = user.get_connection()
        cur = conn.cursor()
        # lets run the query we made
        cur.execute(user_table)

        # lets truncate the table so we always start out with 5 users
        cur.execute('DELETE from users;')

        # see if any users exist and grab their emails
        existing_users = cur.execute('SELECT * FROM users;').fetchall()
        user_emails = {user['email'] for user in existing_users}

        # loop over default users and create them
        for default_user in self.get_default_users():

            # lets not recreate existing users in db
            if default_user['email'] in user_emails:
                continue
            create_users = """
            INSERT INTO users (first_name, last_name, email)
            VALUES 
            """

            # create db entry for current user
            create_users += "('{}','{}','{}')".format(default_user['first_name'], default_user['last_name'], default_user['email'])
            cur.execute(create_users)

        # lets save the changes to the db
        conn.commit()
