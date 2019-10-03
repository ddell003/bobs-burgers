#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
David Dell
MET CS 521
09/26/19
Final Project
Description: A python API using the flask web framework
"""

from flask import Flask, jsonify, make_response, abort, request, g
from flask_cors import CORS
from services.user.user_service import UserService
from request_validator import RequestValidator
import sqlite3
from sqlite3 import Error

# configuration
DEBUG = True

DATABASE = 'burgers.db'

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS, needed if setting up a front end app
CORS(app, resources={r'/*': {'origins': '*'}})

# define the services being used
user_service = UserService()

"""
Router:
The below is the router for my API
This page takes in requests and maps them to my services. This page ideally should be kept skinny, and only deal with 
requests and responses
"""


@app.route('/users', methods=['GET'])
def get_users():
    """
    This function makes a call to the user service requesting all users, down the road i can I query strings to give
    user more flexibility with request
    It then calls flask function jsonify which converts the data into json
    Make response is then called which returns a friendly http response with the json and what ever status code you want
    :return:
    """
    return make_response(jsonify(wrap_data(user_service.get_users())))


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):

    user = user_service.get_user(user_id)
    has_item(user)
    return make_response(jsonify(wrap_data(user)))


@app.route('/users', methods=['POST'])
def create_user():

    request_object = RequestValidator(request)

    return make_response(jsonify(wrap_data(user_service.create_user(request_object))), 201)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Lets update the user
    :param user_id:
    :return:
    """
    user = user_service.get_user(user_id)
    has_item(user)
    request_object = RequestValidator(request)
    return make_response(jsonify(wrap_data(user_service.update_user(request_object, user))), 200)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Lets delete the user
    :param user_id:
    :return:
    """
    user = user_service.get_user(user_id)
    has_item(user)

    user_service.delete_user(user)

    return make_response(jsonify({}), 204)

@app.route('/setup/setup_db', methods=['GET'])
def setup_db():
    """
    Set up database, this is bad practice to do it this way but for demo purposes it works
    :return:
    """
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
    conn = get_connection()
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(user_table)

    # lets truncate the table so we always start out with 5 users
    cur.execute('DELETE from users;')

    # see if any users exist and grab their emails
    existing_users = cur.execute('SELECT * FROM users;').fetchall()
    user_emails = {user['email'] for user in existing_users}

    for user in user_service.get_default_users():

        # lets not recreate existing users in db
        if user['email'] in user_emails:
            continue
        create_users = """
        INSERT INTO users (first_name, last_name, email)
        VALUES 
        """
        # create db entry for current user
        create_users += "('{}','{}','{}')".format(user['first_name'], user['last_name'], user['email'])
        cur.execute(create_users)

    # lets save the changes to the db
    conn.commit()

    # lets go grab all users and return them
    all_users = cur.execute('SELECT * FROM users;').fetchall()

    return make_response(jsonify(all_users), 200)

def get_connection():

    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def has_item(item):
    """
    lets check to see if an item was found, if not lets return a 404 to the user
    :param item:
    :return:
    """
    if len(item) == 0:
        abort(404)


def wrap_data(item):

    """
    lets format our response to be inside a data property
    :param item:
    :return:
    """
    return {'data': item}


def dict_factory(cursor, row):
    """
    Database helper function
    :param cursor:
    :param row:
    :return:
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


"""
Error Handlers:

The below are extension of the error handling methods by flask, I extended these functions so I can overwrite custom
data and messages. The main reason behind extending these methods is that flask will try to return an html error 
response message, this is an API, we want a json response message
"""
@app.errorhandler(404)
def not_found(error):
    """
    By default, flask will try to return an html error response message, this is an API, we want a json response message
    Lets return a simple 404 message
    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def not_found(error):
    """
    By default, flask will try to return an html error response message, this is an API, we want a json response message
    Lets return a simple 400 message
    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(422)
def not_found(error):
    """
    By default, flask will try to return an html error response message, this is an API, we want a json response message
    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'The following fields (s) are required: '+error.description}), 422)

if __name__ == '__main__':
    app.run()
