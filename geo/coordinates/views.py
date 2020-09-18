from django.http import JsonResponse
from coordinates.models import Coordinate
from coordinates.utils.coordinate import CoordinateObj
from coordinates.utils.queryset import from_queryset_to_list_of_tuples, save_request_history


def find_coordinates(request):
    operation = request.GET.get("operation")
    x = request.GET.get("x")
    y = request.GET.get("y")
    points = request.GET.get("points")
    #  save_request_history(request.get_raw_uri(), x, y, points, operation)
    coordinate_to_query = from_queryset_to_list_of_tuples(Coordinate.objects.all())
    original_query = coordinate_to_query.copy()
    indexes = []
    for point in range(0, int(points)):
        closest_index = getattr(CoordinateObj, f"get_{operation}")(
            coordinate_to_query, (x, y)
        )
        indexes.append(closest_index)
        coordinate_to_query.pop(closest_index)

    response = [original_query[index] for index in indexes]
    return JsonResponse({"result": response})
