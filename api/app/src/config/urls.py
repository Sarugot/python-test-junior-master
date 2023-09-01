from django.urls import path, include
from src.app.controller import TestController, AlgorithmView

urlpatterns = [
    path('test/', TestController.as_view({'get': 'get_result'})),
    path('api/v1/',
         AlgorithmView.as_view({'get': 'get_events', 'post': 'post_event'})),
]