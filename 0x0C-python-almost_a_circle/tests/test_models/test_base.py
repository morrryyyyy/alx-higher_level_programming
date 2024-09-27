#!/usr/bin/python3
"""This is the test_base module.
It defines unittests for the base model.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_args(self):
        b1 = Base(3)
        b2 = Base(12)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 12)

    def test_mixed_args(self):
        b1 = Base()
        b2 = Base(23)
        b3 = Base(32)
        b4 = Base()
        b5 = Base(6)
        self.assertEqual(b1.id, b4.id - 1)
        self.assertEqual(b2.id, 23)
        self.assertEqual(b3.id, 32)
        self.assertEqual(b5.id, 6)

    def test_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_negative(self):
        b1 = Base(-12)
        b2 = Base()
        self.assertEqual(b1.id, -12)
        self.assertEqual(b2.id, 1)

    def test_non_integer_id(self):
        with self.assertRaises(TypeError):
            b1 = Base("1")
        with self.assertRaises(TypeError):
            b2 = Base(9.56)
            