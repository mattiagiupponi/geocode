from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse


@login_required(login_url='/admin/login/')
def index(request):
    return HttpResponse("Welcome to this Example, those are the api available")


@login_required(login_url="admin/login/")
def find_closest_neighbour(request):
    return JsonResponse({"ciao": 223})
