from datetime import datetime

from django.http import JsonResponse
from coordinates.models import Coordinate, RequestHistory
from coordinates.utils.coordinate import CoordinateObj
from coordinates.utils.queryset import from_queryset_to_list_of_tuples


def find_coordinates(request):
    operation = request.GET.get("operation")
    x = request.GET.get("x")
    y = request.GET.get("y")
    points = request.GET.get("points")

    save_history = RequestHistory(
        request="", timestamp=datetime.utcnow(), x_axes=x, y_axes=y, points=points
    )
    save_history.save()
    coordinate_to_query = from_queryset_to_list_of_tuples(Coordinate.objects.all())
    closest_index = getattr(CoordinateObj, f"get_{operation}")(
        coordinate_to_query, (x, y)
    )
    return JsonResponse({"result": coordinate_to_query[closest_index]})
