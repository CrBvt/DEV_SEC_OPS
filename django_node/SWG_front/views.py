import textwrap
import time

import requests

from django.shortcuts import render

from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

ENGINE_URL = settings.ENGINE_URL


class SWG_FrontHomeView(TemplateView):
    """ Sewing Front HomeView """
    template_name = 'SWG_front/swg_front_home.html'


