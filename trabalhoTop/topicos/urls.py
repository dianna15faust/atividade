from django.urls import path
from .views import *

urlpatterns = [
    path('pagina/', IndexView.as_view(), name="index"),
]
