from .views import HomeTemplateView
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.HomeTemplateView.as_view(), name='index'),
]
