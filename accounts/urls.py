from django.urls import path
from . import views
from HD_detection import views


urlpatterns = [
    path("", views.userhome, name="userhome"),
]
