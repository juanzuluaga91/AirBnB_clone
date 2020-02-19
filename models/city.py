#!/usr/bin/python3

"""
inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class that define City"""
    state_id = ""
    name = ""
