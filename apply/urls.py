from django.urls import path
from .views import ApplyView

urlpatterns = [
    path('', ApplyView.as_view(), name='apply'),
]