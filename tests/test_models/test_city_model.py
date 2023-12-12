#!/usr/bin/python3
"""
unittest for the city module
"""

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    unittest for the city class
    """

    def test_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_str_representation(self):
        city = City()
        expected = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(city.__str__(), expected)


    def test_instances(self):
        city = City()
        self.assertIs(type(city), City)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.id, str)

    def test_city_save(self):
        city = City()
        updated_before_save = city.updated_at
        city.save()
        updated_after_save = city.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)

    def test_city_to_dict(self):
        city = City()
        T_format = "%Y-%m-%dT%H:%M:%S.%f"
        city.name = "Intropinko"
        city.number = 7

        self.assertIn("name", city.to_dict())
        self.assertIn("number", city.to_dict())
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())
        self.assertEqual(city.to_dict()["created_at"], city.created_at.strftime(T_format))

    
