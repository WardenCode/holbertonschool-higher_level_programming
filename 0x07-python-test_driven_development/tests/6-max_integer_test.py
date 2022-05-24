#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Set of test to validate the functionality of the function max integer"""
    def test_max(self):
        """Test normal cases without error"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 5, 1, 1, 3, 1, 2, 1, 5]), 5)
        self.assertEqual(max_integer([-1, -5, -1, -1, -3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 319e520, 5]), 319e520)
        self.assertEqual(max_integer(['h', 'a', 'z']), 'z')
        self.assertEqual(max_integer([True, False, True]), True)

    # def test_values(self):
    #     """Test error cases, passing a bad value in the list"""
    #      self.assertRaises(ValueError, max_integer([1, 'test', 2, 5]))
    #     self.assertRaises(ValueError, max_integer([1, 5.60, 2, 5]))
    #     self.assertRaises(ValueError, max_integer([1, {}, 2, 5]))
    #     self.assertRaises(ValueError, max_integer([1, [], 2, 5]))
    #     self.assertRaises(ValueError, max_integer([1, (), 2, 5]))
    #     self.assertRaises(ValueError, max_integer([1, float('nan'), 2, 5]))

    # def test_types(self):
    #     """
    #     Test error cases, passing other type that isn't list, like argument
    #     """
    #     self.assertRaises(TypeError, max_integer(5))
    #     self.assertRaises(TypeError, max_integer(None))
    #     self.assertRaises(TypeError, max_integer(50.20))
    #     self.assertRaises(TypeError, max_integer(''))
    #     self.assertRaises(TypeError, max_integer({}))
    #     self.assertRaises(TypeError, max_integer(()))
    #     self.assertRaises(TypeError, max_integer(float('nan')))
