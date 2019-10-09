#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
David Dell
MET CS 521
10/03/19
Database helpers
"""


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

