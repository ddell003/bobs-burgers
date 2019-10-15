#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
David Dell
MET CS 521
09/26/19
Final Project
Description: A python API using the flask web framework
A class with 1 private 2 public attributes and methods
"""

from flask import abort


class RequestValidator:
    """
    This class validates user input for a given model
    It gets initiated with a request and when ready to be validated it takes in a model
    """

    def __init__(self, request):


        self.request = request
        self.validate_json()
        # fields that dont need validation on
        self.__ignoreables = ['deleted']

    def __repr__(self):

        return repr('Request Validator')

    def validate_json(self):

        """
        lets validate that the request is json
        :return:
        """

        if not self.request.json:
            abort(400, 'Expects a json response')
            # or not 'title' in request.json:

    def validate_fields(self, model):

        """
        lets validate that the request has the required model fields
        :param model:
        :return:
        """

        for field in model.fields:
            if field not in self.request.json and field not in self.__ignoreables:
                self.__throw_error(422, field)

    def __throw_error(self, status_code, message):
        """
        Lets throw some error with a message to send back to the user
        :param status_code:
        :param message:
        :return:
        """
        abort(status_code, message)
