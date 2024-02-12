#!/usr/bin/python3
"""test for model/base.py"""
import unittest
from models.base import Base


class TestBaseInstatiation(unittest.TestCase):
    """Testing Base Instatiation"""

    def test_no_args(self):
        """with no argument"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_id(self):
        """test with id"""
        b1 = Base(12)
        self.assertEqual(b1.id, Base(12).id)

    def test_three_with_a_unique(self):
        """test three with a unique id"""
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertNotEqual(b3.id, b2.id + 1)

    def test_string_instance(self):
        """test for type string instance"""
        self.assertEqual("Hello", Base("Hello").id)

    def test_get_instance(self):
        """assurance that instance cannot be get"""
        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)

    def test_none_instance(self):
        """test for None instance"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_for_float(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_for_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_for_dict(self):
        self.assertEqual({'a': 2, 'b': 3}, Base({'a': 2, 'b': 3}).id)

    def test_for_complex(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_for_range(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
