""" Home urls """

from django.urls import path

from . import views

urlpatterns = [
    path('home', views.SWG_FrontHomeView.as_view(), name='SWG_front.home'),
]
