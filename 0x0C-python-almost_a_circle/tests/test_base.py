import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''resets __nb_objects before each test'''
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignd_when_provided(self):
        '''test that the id is correctly assigned when provided'''
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_auto_incremrnted(self):
        '''test that id is auto-incremented when not provided'''
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_mixed(self):
        '''test that id is properly assigned when mixed'''
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

    def test_nb_objects_private(self):
        '''test that __nb_objects is private and not accessible'''
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
