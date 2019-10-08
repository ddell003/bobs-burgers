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
from request_validator import RequestValidator
import sqlite3
from services.user.user_service import UserService
from services.menu.menu_service import MenuService
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
menu_service = MenuService()

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
    """
    url to get a specific user gets mapped here, we then call the userservice to process request
    :param user_id:
    :return:
    """
    # get the user
    user = user_service.get_user(user_id)
    # see if a user was found
    has_item(user)
    # return user object to client
    return make_response(jsonify(wrap_data(user)))


@app.route('/users', methods=['POST'])
def create_user():
    """
    Url to create a user gets mapped to this function
    :return:
    """
    # lets validate the input the client sent to us
    request_object = RequestValidator(request)
    # lets call the userservice to create the user and then return the created user to the client
    return make_response(jsonify(wrap_data(user_service.create_user(request_object))), 201)


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Lets update the user
    :param user_id:
    :return:
    """
    # lets get the user we are updating
    user = user_service.get_user(user_id)
    # make sure the user being updated exists
    has_item(user)
    # validate the update data
    request_object = RequestValidator(request)
    # go update the user and return updated object to client with a 200 response
    return make_response(jsonify(wrap_data(user_service.update_user(request_object, user))), 200)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Lets delete the user
    :param user_id:
    :return:
    """
    # see if user being deleted exists
    user = user_service.get_user(user_id)
    has_item(user)
    # go perform delete operation
    user_service.delete_user(user)
    # return empty 204 response to client, no data to return since the user was deleted
    return make_response(jsonify({}), 204)

@app.route('/menu_sections', methods=['GET'])
def get_menu_sections():
    """
    This function makes a call to the menu service requesting all sections, down the road i can I query strings to give
    user more flexibility with request
    It then calls flask function jsonify which converts the data into json
    Make response is then called which returns a friendly http response with the json and what ever status code you want
    :return:
    """
    return make_response(jsonify(wrap_data(menu_service.get_menu_sections())))

@app.route('/menu_sections/<int:section_id>', methods=['GET'])
def get_menu_section(section_id):
    """
    url to get a specific section gets mapped here, we then call the menu service to process request
    :param section_id:
    :return:
    """
    # get the section
    item = menu_service.get_section(section_id)
    # see if a section was found
    has_item(item)
    # return user object to client
    return make_response(jsonify(wrap_data(item)))

@app.route('/api/menu_items', methods=['GET'])
def get_menu_items():
    """
    This function makes a call to the menu service requesting all items
    It then calls flask function jsonify which converts the data into json
    Make response is then called which returns a friendly http response with the json and what ever status code you want
    :return:
    """
    return make_response(jsonify(wrap_data(menu_service.get_menu_items())))

@app.route('/api/menu_items/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    """
    url to get a specific item gets mapped here, we then call the menu service to process request
    :param item_id:
    :return:
    """
    # get the section
    item = menu_service.get_item(item_id)
    # see if a section was found
    has_item(item)
    # return user object to client
    return make_response(jsonify(wrap_data(item)))

@app.route('/setup/setup_db', methods=['GET'])
def setup_db():
    """
    Set up database, this is bad practice to do it this way but for demo purposes it works
    :return:
    """
    # lets create the users table and load some default users in
    user_service.set_up_users()
    menu_service.set_up_sections()
    menu_service.set_up_items()
    data = {
        'users': user_service.get_users(),
        'menu_sections' : menu_service.get_menu_sections(),
        'menu_items' : menu_service.get_menu_items(),
    }
    return make_response(jsonify(wrap_data(data)))


def get_connection():
    """
    function used to connect to sqlite file database, we then save this info in the global to be used later in app on
    same connection
    :return:
    """
    try:
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect('burgers.db')
        return db
    except:
        # if we cant connect lets throw a 500 with an error message
        abort(500, 'Issue Connecting to the database')

@app.teardown_appcontext
def close_connection(exception):
    """
    sqlite is a file so we need to close it when we are done with it, this ensures that its always closed
    :param exception:
    :return:
    """
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
