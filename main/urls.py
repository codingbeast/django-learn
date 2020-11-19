from django.urls import path, include
from .views import Register
urlpatterns = [
    path('', Register, name="register")
]