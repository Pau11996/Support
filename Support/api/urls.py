from django.contrib import admin
from django.urls import path, include

from .views import BaseView

urlpatterns = [
    path('', BaseView.as_view())
]