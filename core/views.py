from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = AboutMe.objects.first()
        context['works'] = RecentWork.objects.all()
        context['services'] = Service.objects.all()
        return context
