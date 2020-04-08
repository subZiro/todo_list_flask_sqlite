# -*- coding: utf-8 -*-

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from config import Configuration


# --иниц flask приложения-- #
app = Flask(__name__)

# --настройки-- #
app.config.from_object(Configuration)

# --подключение к бд через sqlalchemy--#
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        """корректный вывод"""
        return f'<Task: {self.content}>'
