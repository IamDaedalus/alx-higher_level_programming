#!/usr/bin/python3

"""Test module for Rectangle"""

from io import StringIO
import sys
import unittest
from models.rectangle import Rectangle


class RectangleTests(unittest.TestCase):
    """Tests for Rectangle class."""
    def setUp(self):
        self.rect = Rectangle(15, 20)

    def test_width(self):
        """Testing width"""
        self.assertEqual(self.rect.width, 15)

    def test_height(self):
        """Testing height"""
        self.assertEqual(self.rect.height, 20)

    def test_x_val(self):
        """testing the x value"""
        self.rect.x = 0
        self.assertEqual(self.rect.x, 0)

    def test_y_val(self):
        """testing the x value"""
        self.rect.y = 0
        self.assertEqual(self.rect.y, 0)

    def test_x_neg(self):
        """testing assigning neg to x"""
        with self.assertRaises(ValueError):
            self.rect.x = -1

    def test_y_neg(self):
        """testing assigning neg to y"""
        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_width_zero(self):
        """testing assigning 0 to width"""
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def test_height_zero(self):
        """testing assigning 0 to height"""
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_string_assign_width(self):
        """test assigning string to width"""
        with self.assertRaises(TypeError):
            self.rect.width = "4"

    def test_string_assign_height(self):
        """test assigning string to height"""
        with self.assertRaises(TypeError):
            self.rect.height = "4"

    def test_bool_assign_width(self):
        """test assigning bool to width"""
        with self.assertRaises(TypeError):
            self.rect.width = True

    def test_bool_assign_height(self):
        """test assigning bool to height"""
        with self.assertRaises(TypeError):
            self.rect.height = True

    def test_none_assign_width(self):
        """test assigning None to width"""
        with self.assertRaises(TypeError):
            self.rect.width = None

    def test_none_assign_height(self):
        """test assigning None to height"""
        with self.assertRaises(TypeError):
            self.rect.height = None

    def test_float_assign_width(self):
        """testing assigning float value to width"""
        with self.assertRaises(TypeError):
            self.rect.width = 7.8

    def test_float_assign_height(self):
        """testing assigning float value to height"""
        with self.assertRaises(TypeError):
            self.rect.height = 7.8

    def test_list_assign_width(self):
        """testing assigning float value to width"""
        with self.assertRaises(TypeError):
            self.rect.width = [8, 9]

    def test_list_assign_height(self):
        """testing assigning float value to height"""
        with self.assertRaises(TypeError):
            self.rect.height = [8, 9]

    def test_string_assign_x(self):
        """test assigning string to x"""
        with self.assertRaises(TypeError):
            self.rect.x = "4"

    def test_string_assign_y(self):
        """test assigning string to y"""
        with self.assertRaises(TypeError):
            self.rect.y = "4"

    def test_bool_assign_x(self):
        """test assigning bool to x"""
        with self.assertRaises(TypeError):
            self.rect.x = True

    def test_bool_assign_y(self):
        """test assigning bool to y"""
        with self.assertRaises(TypeError):
            self.rect.y = True

    def test_none_assign_x(self):
        """test assigning None to x"""
        with self.assertRaises(TypeError):
            self.rect.x = None

    def test_none_assign_y(self):
        """test assigning None to y"""
        with self.assertRaises(TypeError):
            self.rect.y = None

    def test_float_assign_x(self):
        """testing assigning float value to x"""
        with self.assertRaises(TypeError):
            self.rect.x = 7.8

    def test_float_assign_y(self):
        """testing assigning float value to y"""
        with self.assertRaises(TypeError):
            self.rect.y = 7.8

    def test_list_assign_x(self):
        """testing assigning float value to x"""
        with self.assertRaises(TypeError):
            self.rect.x = [8, 9]

    def test_list_assign_y(self):
        """testing assigning float value to y"""
        with self.assertRaises(TypeError):
            self.rect.y = [8, 9]

    def test_id(self):
        """test checking id"""
        r = Rectangle(1, 2, 3, 4, 27)
        self.assertEqual(r.id, 27)

    def test_area(self):
        """testing area"""
        self.assertEqual(self.rect.area(), self.rect.height * self.rect.width)

    def test_normal_update(self):
        """normal testing of the update function"""
        self.rect.update(12, 67, 22, 1, 9)
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.width, 67)
        self.assertEqual(self.rect.height, 22)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 9)

    def test_id_update(self):
        """updating the id using update"""
        self.rect.update(77)
        self.assertEqual(self.rect.id, 77)

    def test_string_id_update(self):
        """updating the id using update"""
        with self.assertRaises(TypeError):
            self.rect.update("77")

    def test_list_id_update(self):
        """test to assigning list to update"""
        with self.assertRaises(TypeError):
            self.rect.update([1, 2, 3, 4])

    def test_float_id_update(self):
        """test to assigning float to update"""
        with self.assertRaises(TypeError):
            self.rect.update(8.9)

    def test_str_str_update(self):
        """test assigning string to update"""
        with self.assertRaises(TypeError):
            self.rect.update(69, "haha", "nice")

    def test_overload_update(self):
        """test passing more than 5 values to update"""
        with self.assertRaises(IndexError):
            self.rect.update(12, 67, 22, 1, 9, 234, 12, 395, 45945)

    def test_kwargs_update(self):
        """test to check the kwargs values are assigned"""
        self.rect.update(y=54, height=65, x=12, width=89, id=89)
        self.assertEqual(self.rect.id, 89)
        self.assertEqual(self.rect.width, 89)
        self.assertEqual(self.rect.height, 65)
        self.assertEqual(self.rect.x, 12)
        self.assertEqual(self.rect.y, 54)

    def test_kwargs_args_update(self):
        """test to put kwargs and args together"""
        self.rect.update(1, 2, 3, height=45)
        self.assertEqual(self.rect.id, 1)
        self.assertEqual(self.rect.width, 2)
        self.assertEqual(self.rect.height, 3)

    def test_str_overload(self):
        """test for string overload"""
        self.rect.update(1, 2, 3, 4, 5)
        self.assertEqual(self.rect.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_negative_width(self):
        """Test assigning a negative width value."""
        with self.assertRaises(ValueError):
            self.rect.width = -5

    def test_negative_height(self):
        """Test assigning a negative height value."""
        with self.assertRaises(ValueError):
            self.rect.height = -5

    def test_area_after_attribute_change(self):
        """Test area is correctly updated after changing width and height."""
        self.rect.width = 10
        self.rect.height = 5
        self.assertEqual(self.rect.area(), 50)

    def test_dict_representation(self):
        """Test converting a Rectangle to a dictionary."""
        self.rect.update(1, 15, 20, 5, 0)
        expected_dict = {
            'x': 5,
            'y': 0,
            'id': 1,
            'height': 20,
            'width': 15,
        }
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

    def tearDown(self):
        del self.rect


class TestRectangleDisplay(unittest.TestCase):
    """module to test display method"""
    def setUp(self):
        """Redirect stdout to capture the printed output"""
        self.saved_stdout = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        """Restore the original stdout"""
        sys.stdout = self.saved_stdout

    def test_display_no_offset(self):
        """tesing no display offset"""
        r = Rectangle(3, 2)
        r.display()
        expected_output = "###\n###\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_display_with_offset(self):
        """testing display offset"""
        r = Rectangle(3, 2, 2, 1)
        r.display()
        expected_output = "\n  ###\n  ###\n"
        self.assertEqual(self.output.getvalue(), expected_output)

    def test_display_empty_rectangle(self):
        """testing empty rectangle"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 0)
            r.display()


class TestValidateValue(unittest.TestCase):
    """Tests for Rectangle methods."""

    def test_validate_value_positive(self):
        """Test validate_value with positive integer value."""
        rect = Rectangle(10, 20)
        validated_value = rect._Rectangle__validate_value("test_attr", 5, int)
        self.assertEqual(validated_value, 5)

    def test_validate_value_zero(self):
        """Test validate_value with zero value."""
        rect = Rectangle(10, 20)
        validated_value = rect._Rectangle__validate_value(
                "test_attr", 0, int, min=0
                )
        self.assertEqual(validated_value, 0)

    def test_validate_value_negative(self):
        """Test validate_value with negative value."""
        rect = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            rect._Rectangle__validate_value("test_attr", -5, int, min=1)

    def test_validate_value_wrong_type(self):
        """Test validate_value with wrong type value."""
        rect = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rect._Rectangle__validate_value("test_attr", "string_value", int)


if __name__ == "__main__":
    unittest.main()
