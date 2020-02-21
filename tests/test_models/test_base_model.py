#!/usr/bin/python3
"""
Base Model Unittest Module
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
import datetime


class TestBaseModel(unittest.TestCase):
    """Base Model Class Tests"""

    def setUp(self):
        """Sets up method"""
        pass

    def tearDown(self):
        """Tears down methods"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except IOError:
            pass

    def test_basemodel_attr_types(self):
        """Test base model instance attributes"""
        B = BaseModel()
        self.assertEqual(type(B.id), str)
        self.assertTrue(type(B.created_at) is datetime.datetime)
        self.assertTrue(type(B.updated_at) is datetime.datetime)

    def test_basemodel_diff_id(self):
        """Test base model instance different id"""
        B1 = BaseModel()
        B2 = BaseModel()
        B3 = BaseModel()
        self.assertNotEqual(B1.id, B2.id)
        self.assertNotEqual(B1.id, B3.id)
        self.assertNotEqual(B2.id, B3.id)

    def test_basemodel_none_kwargs(self):
        """Test base model none kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_basemodel_save_none(self):
        """Tests save no instances"""
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_basemodel_save(self):
        """Tests save"""
        B = BaseModel()
        B.save()
        k = "{}.{}".format(type(B).__name__, B.id)
        dict = {k: B.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as file:
            self.assertEqual(json.load(file), dict)

if __name__ == '__main__':
    unittest.main()
