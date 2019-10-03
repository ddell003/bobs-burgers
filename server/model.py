import sqlite3
from flask import g

class Model:

    fields = []
    table = None
    soft_delete = False

    def __init__(self):

            for field in self.fields:
                setattr(self, field, None)

    def get(self):
        """
        Go get all entries for a table
        :return:
        """

        # if soft deletes, concate on to query
        delete = ''
        if self.soft_delete:
            delete = ' WHERE deleted = 0'

        # lets build the query
        query = "SELECT * FROM {}{};".format(self.table, delete)
        conn = self.get_connection()
        cur = conn.cursor()

        # lets get all the items
        items = cur.execute(query).fetchall()

        # lets loop over all items and cast them to a dictionary
        readable = []
        for item in items:
            row = dict(zip([c[0] for c in cur.description], item))
            readable.append(row)

        return readable

    def get_by_id(self, user_id):
        """
        lets get an entry
        :return:
        """

        query = "SELECT * FROM {} WHERE id = {};".format(self.table, user_id)
        conn = self.get_connection()
        cur = conn.cursor()
        # lets get all the item
        item = cur.execute(query).fetchall()

        # if item doesnt exist
        if not item:
            return {}

        # otherwise lets make it pretty
        return dict(zip([c[0] for c in cur.description], item[0]))

    def get_connection(self):
        """
        lets connect to the db which is stored in the globals
        :return:
        """
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect('burgers.db')
        return db
