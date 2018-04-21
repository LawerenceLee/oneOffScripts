"""Unittests for chemPy

created by: Zach Owens
"""
import os
import unittest
from unittest.mock import patch
from unittest import TestCase

import chemPy


class TestUnitConvert(TestCase):

    def test_c_to_f_conversion(self):
        assert chemPy.convert_unit(20, "c", "F") == 68
        assert chemPy.convert_unit(-100, "C", "f") == -148

    def test_f_to_c_conversion(self):
        assert chemPy.convert_unit(68, "F", "c") == 20.0
        assert chemPy.convert_unit(-148, "f", "C") == -100

    def test_k_to_c_conversion(self):
        assert chemPy.convert_unit(100, "k", "c") == -173.14999999999998
        assert chemPy.convert_unit(-5.0, "k", "C") == -278.15

    def test_c_to_k_conversion(self):
        assert chemPy.convert_unit(-278.15, 'C', 'K') == -5
        assert chemPy.convert_unit(12, 'C', 'K') == 285.15

    def test_f_to_k_conversion(self):
        assert chemPy.convert_unit(1000, 'f', 'K') == 810.9277777777778
        assert chemPy.convert_unit(-1, 'f', 'k') == 254.81666666666663

    def test_k_to_f_conversion(self):
        assert chemPy.convert_unit(34, 'K', 'f') == -398.46999999999997
        assert chemPy.convert_unit(-134, 'k', 'F') == -700.87


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else "clear")
    unittest.main()
