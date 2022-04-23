from django.shortcuts import render
from django.views.generic.base import TemplateView


class BaseView(TemplateView):

    template_name = "home.html"
