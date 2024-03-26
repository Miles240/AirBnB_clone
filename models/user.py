#!/usr/bin/python3
"""Module for User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class
    Args:
        - email(str): User email
        - password(str): User password
        - first_name(str): User first name
        - last_name(str): User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
