#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class defining test cases for max_integer function."""
    def test_negative(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_normal(self):
        self.assertEqual(max_integer([1, 3, 2, 4, 3]), 4)

    def test_string(self):
        self.assertEqual(max_integer(['1', '2', '3', '4']), '4')

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -7, -5]), -1)

    def test_mixed(self):
        with self.assertRaises(TypeError):
            max_integer(['1', 'a', 2.3, 5])

    def test_repeated(self):
        self.assertEqual(max_integer([1, 4, 2, 4, 3, 4, 1]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.2]), 3.3)
