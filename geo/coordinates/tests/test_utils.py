import unittest
from django.test import TestCase
from coordinates.models import Coordinate
from coordinates.utils.queryset import from_coordinates_qs_to_list, save_request_history


class TestUtils(TestCase):
    def setUp(self) -> None:
        self.coordinate = Coordinate(x_axes=1, y_axes=2)

    def test_from_coordinates_qs_to_list(self):
        sut = [self.coordinate]
        expected = [(1, 2)]
        actual = from_coordinates_qs_to_list(sut)
        self.assertListEqual(expected, actual)

    def test_save_request_history(self):
        actual = save_request_history("foo", 5, 4, 3, "bar")
        self.assertEqual("foo", actual.request)
        self.assertEqual(5, actual.x_axes)
        self.assertEqual(4, actual.y_axes)
        self.assertEqual(3, actual.points)
        self.assertEqual("bar", actual.operation)


if __name__ == '__main__':
    unittest.main()
