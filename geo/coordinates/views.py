from django.http import JsonResponse
from coordinates.models import Coordinate
from coordinates.utils.coordinate import CoordinateObj
from coordinates.utils.queryset import from_queryset_to_list_of_tuples


def find_coordinates(request):
    operation = request.GET.get('operation')
    x = request.GET.get('x')
    y = request.GET.get('y')
    coordinate_to_query = from_queryset_to_list_of_tuples(Coordinate.objects.all())
    closest_index = getattr(CoordinateObj, f"get_{operation}")(coordinate_to_query, (x, y))
    return JsonResponse({operation: coordinate_to_query[closest_index]})
