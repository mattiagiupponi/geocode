import json

from django.test import TestCase
from django.test.client import RequestFactory

from coordinates.models import Coordinate
from coordinates.views import find_coordinates, get_url_parameters


class TestCoordinatesView(TestCase):
    def setUp(self) -> None:
        self.sut = RequestFactory()

    def test_view(self):
        c = Coordinate(
            x_axes=1, y_axes=2
        )
        c.save()
        x = find_coordinates(self.sut.get("/api/test/foo?operation=nearest&x=1&y=2&points=1"))
        self.assertEqual(x.status_code, 200)
        self.assertDictEqual(json.loads(x.content), {"result": [[1.0, 2.0]]})

    def test_will_return_the_expected_parameters(self):
            operation, x, y, points = get_url_parameters(self.sut.get("/api/test/foo?operation=nearest&x=1&y=2&points=1"))
            self.assertEqual("nearest", operation)
            self.assertEqual(1, x)
            self.assertEqual(2, y)
            self.assertEqual(1, points)

    def test_will_raise_an_error_on_missing_param(self):
        c = Coordinate(
            x_axes=1, y_axes=2
        )
        c.save()
        with self.assertRaises(ValueError):
            x = find_coordinates(self.sut.get("/api/test/foo?operation=nearest&x=1&y=2"))
            self.assertEqual(x.status_code, 500)

    def test_will_raise_an_error_on_missing_coordinates(self):
        with self.assertRaises(ValueError):
            x = find_coordinates(self.sut.get("/api/test/foo?operation=nearest&x=1&y=2&points=1"))
            self.assertEqual(x.status_code, 500)

    def test_will_rase_exception_if_some_parameter_is_missing(self):
        with self.assertRaises(ValueError):
            get_url_parameters(self.sut.get("/api/test/foo?operation=nearest"))
