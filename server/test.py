#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
David Dell
MET CS 521
09/26/19
Final Project
Description: Lets use unit tests to assert our api works! ... can also just hit the endpoint /setup/run_tests
"""
from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_status(self):
        """
        lets test we can ping the status page
        :return:
        """
        tester = app.test_client(self)
        response = tester.get('/api/status', content_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'"success!"\n')

    def test_setup(self):
        """
        lets test we can set up a database with users and other pre populated fields
        :return:
        """
        tester = app.test_client(self)
        response = tester.get('/setup/setup_db', content_type='json')
        self.assertEqual(response.status_code, 200)

        data = response.json['data'];
        self.assertEqual(5, len(data['users']))
        self.assertEqual(6, len(data['menu_sections']))
        self.assertEqual(16, len(data['menu_items']))

    def test_user_endpoints(self):
        """
        Test user endpoints
        :return:
        """
        # set up test
        tester = app.test_client(self)
        # set up db
        response = tester.get('/setup/setup_db', content_type='json')
        # assert status code
        self.assertEqual(response.status_code, 200)
        # get list
        users_response = tester.get('/api/users', content_type='json')
        self.assertEqual(users_response.status_code, 200)
        # assert count of list
        user_list = users_response.json['data']
        self.assertEqual(5, len(user_list))

        # get specific user and assert status code 200
        user_response = tester.get('/api/users/1', content_type='json')
        self.assertEqual(user_response.status_code, 200)
        user = user_response.json['data']
        # test user object
        self.assertEqual(user['first_name'], 'Bob')
        self.assertEqual(user['last_name'], 'Belcher')
        self.assertEqual(user['email'], 'bob@bobsburgers.gmail.com')
        self.assertEqual(user['deleted'], 0)

        # test delete
        response = tester.delete('/api/users/1', content_type='json')
        self.assertEqual(response.status_code, 204)

        # get list again
        users_response = tester.get('/api/users', content_type='json')
        self.assertEqual(users_response.status_code, 200)
        # assert count of list is one less now that a user has been deleted
        user_list = users_response.json['data']
        self.assertEqual(4, len(user_list))

    """
    Eventually I would go and make tests for menu, lists and items as well as add in update and create to the user test
    """


if __name__ == '__main__':
    unittest.main()
