import textwrap
import time

import requests

from django.shortcuts import render

from django.views.generic import TemplateView, View
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

ENGINE_URL = settings.ENGINE_URL


class XlToolsHomeView(LoginRequiredMixin, TemplateView):
    """ Xl Tools Home View """
    template_name = 'xl_tools/xl_tools_home.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("SOMEONE IS USING ME")
        context.update({'engine_url': ENGINE_URL, 'engine_status': 'Unknown'})
        return context


class AjaxHandlerView(View):

    def get(self, request): # noqa

        target = request.headers.get('Target-Url')

        r = requests.get(target)
        return JsonResponse(eval(r.text))


