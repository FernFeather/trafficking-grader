from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# trafficking-grader/about/views.py
from companies.models import Companies


class AboutView(TemplateView):
    template_name = 'about/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.today()
        context['companies'] = Companies.objects.all()  # Add this line
        return context
