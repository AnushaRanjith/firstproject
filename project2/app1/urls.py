from django.urls import path
from .views import good_mng

urlpatterns = [
    path('hello/', good_mng),
]
