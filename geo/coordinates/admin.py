from django.contrib import admin

# Register your models here.
from coordinates.models import Coordinate, RequestHistory

admin.site.register(Coordinate)
admin.site.register(RequestHistory)
