import sqlite3
from flask import g


class Model:
    """
    All other models will extend this, we hold the core functionality here
    We interact with the database for the model here
    """
    # default values
    fields = []
    table = None
    # defaulting this to true unless we actually want to hard delete
    soft_delete = True

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

    def create(self, data):
        """
        Lets create the item!
        :param data:
        :return:
        """

        string_fields = ''
        values = ''
        count = 1

        # lets loop over fields building up query
        for field in self.fields:
            if field not in data.keys():
                continue
            comma = ''
            if count < len(data.keys()):
                comma = ','
            string_fields += '{}{}'.format(field, comma)
            values += "'{}'{} ".format(data[field], comma)
            count += 1

        if values == '':
            return False

        string_fields = '({})'.format(string_fields)
        values = '({})'.format(values)

        query = "INSERT INTO {} {} VALUES {}".format(self.table, string_fields, values)

        # connect to db and make entry
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()

        # lets get the id of the item just made
        last_id = cur.execute('SELECT last_insert_rowid()').fetchone()[0]
        # lets get the made entry to return
        entry = self.get_by_id(last_id)
        return entry

    def update(self, id, data):
        """
        Lets update the entry given an id and data
        :param id:
        :param data:
        :return:
        """
        values = ''
        count = 1

        # lets loop over fields building up query so we only update valid fields
        for field in self.fields:
            if field not in data.keys():
                continue
            comma = ''
            if count < (len(data.keys()) - 1):
                comma = ','
            values += "'{}' = '{}'{}".format(field, data[field], comma)
            count += 1

        query = "UPDATE {} SET {} WHERE id = {}".format(self.table, values, id)

        # connect to db and make entry
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()

        # lets get the made entry to return
        entry = self.get_by_id(id)
        return entry

    def delete(self, id):
        """
        lets delete the entry
        :param id:
        :return:
        """
        # no one actually deletes data anymore so we will soft delete this user
        query = "UPDATE {} SET deleted = 1 WHERE id = {}".format(self.table, id)

        # connect to db and make query
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()

    def get_connection(self):
        """
        lets connect to the db which is stored in the globals
        :return:
        """
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect('burgers.db')
        return db
