from utils import arrs

import unittest

class Uni(unittest.TestCase):
    def test_get(self):
        assert arrs.get([1, 2, 3], 1, "test") == 2
        assert arrs.get([], 0, "test") == "test"


    def test_slice(self):
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
