#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
# Example 1
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    
    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0) 
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3) 
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

# Example 2
def median(pool):
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[(size - 1) / 2]
    else:
        return (copy[size/2 -1] + copy[size/2]) / 2

class TakeMedian(unittest.TestCase):
    def test_median(self):
        self.failUnlessEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)

if __name__ == "__main__":
    unittest.main()
