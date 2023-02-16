#!/usr/bin/python3
"""
Defines unittest for base.py
"""

import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """unittest for testing instantiation of Base class"""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b1.id, b3.id - 2)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)

        self.assertEqual(b1.id, b2.id - 1)

    def test_specific_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_id_after_specific(self):
        b1 = Base(10)
        b2 = Base()

        self.assertEqual(b2.id, b1.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 32
        
        self.assertEqual(b.id, 32)
    
    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


class TestBase_to_json_string(unittest.TestCase):
    """Unittest for testing to_json_string method of Base class"""

    def test_to_json_string_rectangle(self):
      rect = Rectangle(1, 2, 3, 4)
      to_string = Base.to_json_string([rect.to_dictionary()])

      self.assertEqual(type(to_string), str)

    def test_to_json_string_square_type(self):
        s = Square(1, 2, 3, 4)
        s_json = Base.to_json_string([s.to_dictionary()])

        self.assertEqual(type(s_json), str)

    def test_to_json_string_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))
    
    def test_to_json_string_no_args(self):
        with self.assertRaises(AttributeError):
            Base.to_json_string()

    def test_to_json_string_many_args(self):
        with self.assertRaises(AttributeError):
                Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Tests for save_to_file method of Base class"""

    @classmethod
    def teardown(self):
        """Deletes all created files"""

        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        
    def test_save_to_file_one(self):
        rect = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertTrue(f.read())

    def test_save_to_file_two(self):
        rect_1 = Rectangle(1, 2, 3, 4)
        rect_2 = Rectangle(5, 6, 7, 8)
        Rectangle.save_to_file([rect_1, rect_2])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertTrue(f.read())
    
    def test_save_to_file_square_one(self):
        square = Square(10, 2, 3, 1)
        Square.save_to_file([square])

        with open("Square.json", "r") as f:
            self.assertTrue(f.read())

    def test_save_to_file_two(self):
        s_1 = Square(1, 2, 3, 4)
        s_2 = Square(5, 6, 7, 8)
        Square.save_to_file([s_1, s_2])

        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertTrue(f.read())

    def test_save_to_file_filename(self):
        s = Square(10, 7, 2, 8)

        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(f.read())

    def test_save_to_file_overwrite(self):
        s = Square(12, 2, 3, 4)
        Square.save_to_file([s])

        s = Square(12, 3, 2, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read())

    def test_save_to_file_none(self):
        Square.save_to_file([None])

        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
    
    def test_save_to_file_empty(self):
        Square.save_to_file([])

        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_more_args(self):
        with self.assertRaises(ValueError):
            Square.save_to_file([], 2)

class TestBase_load_from_file(unittest.TestCase):
    """Tests for testing load_from_file method of Base class"""

    @classmethod
    def teardown(self):
        """Delete any saved file"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        
    def test_load_from_file_rect(self):
        rect = Rectangle(10, 7, 2, 8, 2)

        Rectangle.save_to_file([rect])
        output = Rectangle.load_from_file()
        self.assertEqual(output[0], str(rect))

    def test_load_from_file_rect(self):
        rect = Rectangle(10, 2, 4, 5, 1)
        Rectangle.save_to_file([rect])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_square(self):
        square = Square(10, 7, 2)

        Square.save_to_file(square)
        output = Square.load_from_file()
        self.assertEqual(output[0], str(square))

    def test_load_from_file_square(self):
        square = Square(10, 2, 4,)
        Square.save_to_file(square)
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_args(self):
        with self.assertRaises(ValueError):
            Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()