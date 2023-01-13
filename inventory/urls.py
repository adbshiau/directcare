from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inventory-index"),
    path("staff/", views.staff, name="inventory-staff"),
]