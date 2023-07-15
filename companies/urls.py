from django.urls import path
from . import views

urlpatterns = [
    path('companies', views.CompanyListView.as_view(), name="companies.list"),
    path('companies/<int:pk>', views.CompanyDetailView.as_view(), name="companies.detail")
]