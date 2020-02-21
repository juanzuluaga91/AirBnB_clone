#!/usr/bin/python3
"""
Console Unittest Module
"""
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from unittest.mock import patch
from io import StringIO
import os
import pep8

class TestHBNBCommand(unittest.TestCase):
    """Tests HBNBCommand Console"""

    def setUp(self):
        """Sets up method"""
        pass

    def test_pep8_conformance(self):
        """Tests Pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Fix pep8")
    
    def test_HBNBCommand_help(self):
        """Tests the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        string = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
"""

    def test_HBNBCommand_help_EOF(self):
        """Tests the help EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        string = "EOF command to exit the program\n"
        self.assertEqual(string, f.getvalue())

if __name__ == "__main__":
    unittest.main()
