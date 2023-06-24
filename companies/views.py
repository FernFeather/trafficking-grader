from django.shortcuts import render
from .models import Companies
from django.http import Http404
from django.views.generic import DeleteView, ListView

# companies/companies_list.html'
class CompanyListView(ListView):
     model = Companies
     context_object_name = "companies"
     template_name = 'companies/companies_list.html'

# companies/companies_detail.html
class CompanyDetailView(DeleteView):
     model = Companies
     context_object_name = "company"
     template_name = 'companies/companies_detail.html'
