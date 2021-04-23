#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Database models"""

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)  #unique=True
    last_name = db.Column(db.String, nullable = False)
    hobbies = db.Column(db.String, nullable = True)

    def __repr__(self):  #magic method - do something magic in python
        return "<User %r>" % self.first_name  # %r is returning the raw string
