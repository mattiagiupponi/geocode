from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

from coordinates.models import RequestHistory


@login_required(login_url='/admin/login/')
def index(request):
    return HttpResponse("Welcome to this Example, those are the api available")


@login_required(login_url='/admin/login/')
def get_request_history(request):
    var = RequestHistory.objects.all()
    return JsonResponse(var)
