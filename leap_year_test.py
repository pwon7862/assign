#_*_ coding: utf-8 _*_

import unittest, os
import leap_year


class ImsiTestCase(unittest.TestCase):
    
    def test_leap_year(self) :
        self.assertEqual(leap_year.leap_year(1700), ("평년"))

if __name__ == "__main__":
    unittest.main(verbosity=2)

