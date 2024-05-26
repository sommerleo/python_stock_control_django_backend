from django.urls import path
from .views import *

app_name = "Product"

urlpatterns = [
    path("teste/", TestView.as_view(), name="teste"),
]
