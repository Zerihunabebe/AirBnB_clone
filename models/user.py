#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
from .base_model import BaseModel


class User(BaseModel):
    """Defines attributes for `User`.
    Attributes:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
