from django.urls import path, include
from .views import VRegistro

urlpatterns = [
    path('', VRegistro.as_view(), name = "Autenticacion"),
]