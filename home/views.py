from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from companies.models import Companies
class HomeView(TemplateView):
    template_name = 'home/welecome.html'
    extra_context = {'today': datetime.today()}
    extra_context['companies'] = Companies.objects.all()

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url= '/admin'
