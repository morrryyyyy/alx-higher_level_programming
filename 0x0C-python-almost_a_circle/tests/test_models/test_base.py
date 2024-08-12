#!/usr/bin/python3
'''
Defines unittests for base.py.
Unittest classes:
    TestBase_instantiation
'''

import os
import unittest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    ''' unittests for testing instantiations of Base class'''

    def setUp(self):
        '''reset __nb_objects before each test'''
        Base._Base__nb_objects = 0

    def test_no_args(self):
        '''test for automatic assignment of id'''
        b = Base()
        self.assertEqual(b.id, 1)
    
    def test_one_arg(self):
        '''test for when id is given'''
        b = Base(23)
        self.assertEqual(b.id, 23)

    def test_mixed_args(self):
        '''test when ids are mixed'''
        b1 = Base()
        b2 = Base(100)
        b3 = Base()
        b4 = Base(23)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 23)
        self.assertEqual(b5.id, 3)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

