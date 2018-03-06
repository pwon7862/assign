# -*- coding: utf-8 -*-

import x_fizzbuzz
import unittest

class ImsiTestCase(unittest.TestCase):

    def test_fizzbizz(self) :
        self.assertEqual(x_fizzbuzz.fizzbuzz(10), [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz'])

if __name__ == "__main__":
    unittest.main(verbosity=2)
