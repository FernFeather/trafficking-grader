from django.shortcuts import render
from .models import Companies

def list(request):
    all_Companies = Companies.objects.all()
    return render(request, 'companies/companies_list.html', {'companies': all_Companies})

def detail(request, pk):
    company = Companies.objects.get(pk=pk)
    return render(request, 'companies/companies_detail.html', {'company': company})