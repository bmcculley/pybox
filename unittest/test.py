#!/bin/python3
import unittest
import autograde

class TestGrading(unittest.TestCase):
    """Let's make sure the correct grades are returned"""
    def test_grades(self):
        self.assertEqual(autograde.answer([73, 67, 38, 33]), [75, 67, 40, 33])

if __name__ == '__main__':
    unittest.main()