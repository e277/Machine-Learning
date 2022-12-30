import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_lngth_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square('5')

    def test_length_is_not_zero_or_negative(self):
        with self.assertRaises(ValueError):
            square = Square(0)
        with self.assertRaises(ValueError):
            square = Square(-1)

if __name__ == "__main__":
    unittest.main()


# To Run all test:
# # python -m unittest
# # python -m unittest -v