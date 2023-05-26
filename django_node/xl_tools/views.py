import requests

from django.shortcuts import render

from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

ENGINE_URL = settings.ENGINE_URL


class XlToolsHomeView(LoginRequiredMixin, TemplateView):
    """ Xl Tools Home View """
    template_name = 'xl_tools/xl_tools_home.html'
    login_url = '/login'

    # r = requests.get(ENGINE_URL)

    extra_context = {'engine_url': ENGINE_URL, 'api_status': 'Unknown'}
