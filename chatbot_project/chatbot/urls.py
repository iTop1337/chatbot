from django.urls import path
from . import views

urlpartterns = [
    path('message/', views.receive_message, name = 'receive_message'),
]