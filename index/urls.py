from django.urls import path

from index.views import home

urlpatterns = [
    path("", home),
]
