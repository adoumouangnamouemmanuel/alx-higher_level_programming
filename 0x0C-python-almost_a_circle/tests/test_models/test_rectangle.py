#!/usr/bin/python3
"""test the rectangle model"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestRectangleInstance(unittest.TestCase):
    """test for rectangle class"""

    def test_for_instance(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg_with_no_id(self):
        b1 = Rectangle(1, 2)
        b2 = Rectangle(2, 1)
        self.assertEqual(b1.id, b2.id - 1)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
             print(Rectangle(1, 2, 3, 4).__y)

    def test_y_get(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter_not_int(self):
        r = Rectangle(5, 7, 7, 5, 1)
        with self.assertRaises(TypeError):
            r.y ="hello"

    def test_y_setter_less(self):
        r = Rectangle(5, 7, 7, 5, 1)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestAReaRectangle(unittest.TestCase):
    """Test for Area of Rectangle"""

    def test_area_with_pre(self):
        r = Rectangle(10, 2)
        self.assertEqual(20, r.area())

    def test_area_with_other(self):
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r.area())

    def test_area_with_modify(self):
        r = Rectangle(9, 3)
        r.width = 10
        self.assertEqual(30, r.area())

    def test_arear_height(self):
        r = Rectangle(9, 3)
        r.height = 10
        self.assertEqual(90, r.area())

    def test_arear_both(self):
        r = Rectangle(1, 2)
        r.width = 11
        r.height = 10
        self.assertEqual(110, r.area())


class TestRectangle_stdout(unittest.TestCase):
    """test fot stdout of display"""

    @staticmethod
    def capture_stdout(rec, method):
        """capture the stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rec)
        else:
            rec.display()
        sys.stdout = sys.__stdout__
        return(capture)

     ##test display
    def test_display_width(self):
        """test the display"""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_height(self):
        """test the display"""
        r = Rectangle(4, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("####\n####\n####\n", capture.getvalue())

    def test_print_a(self):
        r = Rectangle(1, 2, 3, 4, 5)
        m = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(m, r.__str__())

    def test_print_b(self):
        r = Rectangle(1, 2, id=5)
        m = "[Rectangle] (5) 0/0 - 1/2"
        self.assertEqual(m, str(r))


class TestUpdate(unittest.TestCase):
    """test update"""

    def test_update_a(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(5, 4, 3, 2, 1)
        m = "[Rectangle] (5) 2/1 - 4/3"
        self.assertEqual(m, str(r))

    def test_update_b(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        m = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(m, str(r1))

    def test_update_c(self):
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89, 2)
        m = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(m, str(r2))

    def test_update_with_kwargs(self):
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(id = 89)
        m = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(m, str(r3))

    def test_with_arg_kwargs(self):
        r4 = Rectangle(1, 2, 3, 4, 5)
        r4.update(5, 4, 3, 2, 1, id = 90, width = 48)
        m = "[Rectangle] (5) 2/1 - 4/3"
        self.assertEqual(m, str(r4))

    def test_kwargs_only(self):
        r5 = Rectangle(1, 2, 3, 4, 5)
        r5.update(width = 49, height = 40, x = 2, y = 3, id = 7)
        self.assertEqual(r5.area(), 1960)


class TestToDictionary(unittest.TestCase):
    """Rectangle To Dictionary"""

    def test_to_dict_first(self):
        s1 = Rectangle(2, 4)
        s1.id = 8
        p = {'id': 8, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        self.assertEqual(s1.to_dictionary(), p)

    def test_to_dict_with_edit(self):
         s1 = Rectangle(2, 4, 5, 6, 7)
         s1.update(6, 5, 4, 5, 6)
         p = {'id': 6, 'width': 5, 'height': 4, 'x': 5, 'y': 6}
         self.assertEqual(s1.to_dictionary(), p)


class TestToJson(unittest.TestCase):
    """Test  for to json"""
    def test_json_first_a(self):
        r1 = Rectangle(10, 7, 2, 8, 9)
        dictionary = r1.to_dictionary()
        p = '[{"x": 2, "width": 10, "id": 9, "height": 7, "y": 8}]'
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), type(p))

    def test_json_first_b(self):
        dictionary = []
        p = '[[]]'
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, p)
