from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.receive_message, name = 'receive_message'),
]