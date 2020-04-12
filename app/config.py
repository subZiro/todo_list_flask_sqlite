# -*- coding: utf-8 -*-
# config file

class Configuration(object):
    # --debug mode-- #
    # host='0.0.0.0', debug=True, port=80
 
    # --db connect-- #
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'

    SECRET_KEY = 'verrrrry secret key'