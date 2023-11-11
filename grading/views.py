from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class GradingView(TemplateView):
    template_name = 'grading/grading.html'