import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_is_instance(self):
        self.assertIsInstance(Rectangle, Base)

    def test_all_params(self):
        r = Rectangle(10, 20, 5, 5, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 99)

    def test_default_id(self):
        r = Rectangle(10, 20, 5, 5)
        self.assertEqual(r.id, 1)

    def test_private_attributes(self):
        r = Rectangle(10, 20, 5, 5, 99)
        with self.assertRaises(AttributeError):
            print(r.__width)
        with self.assertRaises(AttributeError):
            print(r.__height)
        with self.assertRaises(AttributeError):
            print(r.__x)
        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_invalid_width(self):
        """Test that invalid width raises errors."""
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(ValueError):
            Rectangle(0, 20)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)

    def test_invalid_height(self):
        """Test that invalid height raises errors."""
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, -20)

    def test_invalid_x(self):
        """Test that invalid x raises errors."""
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "5")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5)

    def test_invalid_y(self):
        """Test that invalid y raises errors."""
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "5")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)
