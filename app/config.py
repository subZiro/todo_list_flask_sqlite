# -*- coding: utf-8 -*-
# config file

class Configuration(object):
    # --debug mode-- #
    DEBUG = True

    # --db connect-- #
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'

    SECRET_KEY = 'verrrrry secret key'