from django.http import JsonResponse
from coordinates.models import Coordinate
from coordinates.utils.coordinate import CoordinateObj
from coordinates.utils.queryset import from_coordinates_qs_to_list, save_request_history


def find_coordinates(request):
    operation, x, y, points = get_url_parameters(request)

    save_request_history(request.get_raw_uri(), x, y, points, operation)

    coordinate_to_query = from_coordinates_qs_to_list(Coordinate.objects.all())

    original_query = coordinate_to_query.copy()
    indexes = []
    for point in range(0, points):
        closest_index = getattr(CoordinateObj, f"get_{operation}")(
            coordinate_to_query, (x, y)
        )
        indexes.append(closest_index)
        coordinate_to_query.pop(closest_index)

    response = [original_query[index] for index in indexes]
    return JsonResponse({"result": response})


def get_url_parameters(request):
    try:
        operation = request.GET.get("operation")
        x = float(request.GET.get("x"))
        y = float(request.GET.get("y"))
        points = int(request.GET.get("points"))
        return operation, x, y, points
    except Exception as e:
        raise ValueError("One or more required parameters are empty")
