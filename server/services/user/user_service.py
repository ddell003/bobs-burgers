import pickle
from services.user.models.user import User


class UserService:
    """
    Using a Service Repository Pattern
    Service is where all the business logic takes place - what do we want to do with the user data
    Repository sites on top of a database - file or array
    Model represents a database entity - the user
    """
    user_file_path = 'services/user/users.txt'

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
        found_user = {}

        for user in self.get_users():
            if int(user['id']) == user_id:
                found_user = user
                break
        return found_user

    def create_user(self, request_validator):
        """
        Lets create the user
        :param request_validator:
        :return:
        """
        user = User()
        request_validator.validate_fields(user)

        data  = request_validator.request.json
        data['id'] = str(int(self.get_users()[-1]['id']) + 1)
        data['deleted'] = 0

        self.get_users().append(data)

        return data

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

        # get the input data from the request
        user_data = request_validator.request.json
        # we only want to update certain fields
        user['first_name'] = user_data['first_name']
        user['last_name'] = user_data['last_name']
        user['email'] = user_data['email']

        # lest update this user now
        self.get_users()[int(user['id']) - 1] = user

        return user

    def delete_user(self, user):
        """
        Lets mark this user as deleted
        :param user:
        :return:
        """
        # no one actually deletes data anymore so we will soft delete this user
        user['deleted'] = 1
        # lest update this user now
        self.get_users()[int(user['id']) - 1] = user
