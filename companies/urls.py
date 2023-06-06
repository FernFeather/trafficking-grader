from django.urls import path
from . import views

urlpatterns = [
    path('companies', views.list),
    path('companies/<int:pk>', views.detail)
]