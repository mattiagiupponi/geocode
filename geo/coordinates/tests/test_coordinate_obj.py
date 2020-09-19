import unittest
from coordinates.utils.coordinate import CoordinateObj


class TestCoordinateObj(unittest.TestCase):
    def setUp(self) -> None:
        self.sut = CoordinateObj
        self.dataset = [(1, 1), (2, 2), (3, 3), (4, 4)]
        self.coordinate = (2, 2)

    def test_get_nearest_index(self):
        actual = self.sut.get_nearest(self.dataset, self.coordinate)
        self.assertEqual(actual, 1)

    def test_get_furthest_index(self):
        actual = self.sut.get_furthest(self.dataset, self.coordinate)
        self.assertEqual(actual, 3)


if __name__ == "__main__":
    unittest.main()
