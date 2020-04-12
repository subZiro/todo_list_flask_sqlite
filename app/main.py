# -*- coding: utf-8 -*-
# todo list main

from app import app
#from app import db
import view


# --run programm-- #
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
