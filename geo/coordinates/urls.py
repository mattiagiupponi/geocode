from django.urls import path

from . import views

urlpatterns = [path("", views.find_coordinates, name="find_closest_neighbour")]
