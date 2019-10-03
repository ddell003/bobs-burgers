from model import Model

import sqlite3

class User(Model):

    fields = [
        'first_name',
        'last_name',
        'email',
        'deleted'
    ]

    soft_delete = True
    table = 'users'

    def __init__(self):

        for field in self.fields:
            setattr(self, field, None)


    def __repr__(self):

        return repr('User')


    #def create(self data):

    def dict_factory(self, cursor, row):
        """
        Database helper function
        :param cursor:
        :param row:
        :return:
        """
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]





