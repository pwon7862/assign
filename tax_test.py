#_*_ coding: utf-8 _*_

import unittest, os
import tax


class ImsiTestCase(unittest.TestCase):


    def test_tax(self) :
        self.assertEqual(tax.tax(30, 10000, 1), (1800.0))

if __name__ == "__main__":
    unittest.main(verbosity=2)
