#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample python code that creates users and displays them."""

from app import db, User

def create_my_user(first_name, last_name, hobbies):
    """Simple user creation function"""
    db.session.add(
        User(
            first_name = first_name,
            last_name = last_name,
            hobbies = hobbies
        )
    )

    db.session.commit()


# def update_my_user(id, first_name, last_name, hobbies):
#     """Simple user update function"""
#     db.session.update(
#         User(

#             first_name = first_name,
#             last_name = last_name,
#             hobbies = hobbies
#         )
#     )


#session.delete()
#models.session.new
#jethro.nickname = 'Jetty'
#models.session.dirty
#models.session.commit()

#models.session.query(models.User).order_by(models.Users.column).all()

if __name__ == "__main__":
    create_my_user("Tom", "Nguyen", "Books")
    users = User.query.all()
    print(users)
    create_my_user("John", "Doe", "Golfing")
    user = User.query.filter_by(first_name = "John").first()
    print(user)