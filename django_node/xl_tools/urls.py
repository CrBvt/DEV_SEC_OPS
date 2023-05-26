""" Home urls """

from django.urls import path

from . import views

urlpatterns = [
    path('home', views.XlToolsHomeView.as_view(), name='xl_tools.home'),
    path('ajax', views.AjaxHandlerView.as_view(), name='xl_tools.ajax')
]
