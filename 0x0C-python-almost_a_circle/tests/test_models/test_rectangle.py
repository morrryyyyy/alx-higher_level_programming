#!/usr/bin/python3
"""This is the test_rectangle module.
It defines unittests for the rectangle model.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(1, 1, 0, 0)
        self.rect2 = Rectangle(13, 11, 3, 4)
        self.rect3 = Rectangle(3, 5, 3, 4)


    def test_attrs(self):
        self.assertEqual(self.rect.width, 1)
        self.assertEqual(self.rect.height, 1)
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect.y, 0)

    def test_more_attrs(self):
        self.assertEqual(self.rect2.width, 13)
        self.assertEqual(self.rect2.height, 11)
        self.assertEqual(self.rect2.x, 3)
        self.assertEqual(self.rect2.y, 4)

    def test_non_integer_attrs(self):
        with self.assertRaises(TypeError):
            Rectangle("1", "2", "0", "0")
            Rectangle("1", 2, 0, 0)
            Rectangle(1, "2", 0, 0)
            Rectangle(1, 2, "0", 0)
            Rectangle(1, 2, 0, "0")

    def test_negative_attrs(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 5)
            Rectangle(2, -3, 3, 5)
            Rectangle(0, 2, -3, 5)
            Rectangle(0, 2, 3, -5)

    def test_zero_attrs(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 4, 3)
            Rectangle(12, 0, 4, 3)

    def test_normal_area(self):
        self.assertEqual(self.rect3.area(), 15)