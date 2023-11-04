from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.GradingView.as_view(), name='grading')
]