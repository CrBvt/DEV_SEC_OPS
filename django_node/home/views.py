""" Home views """

from datetime import datetime

# from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect


class SignupView(CreateView):
    """ Sign-up View """
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')

        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    """ Logout View """
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    """ Login View """
    template_name = 'home/login.html'


class HomeView(TemplateView):
    """ Homepage View """
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AppMenuView(LoginRequiredMixin, TemplateView):
    """ AppMenu View """
    login_url = '/login'
    template_name = 'home/app_menu.html'

# class AuthorizedView(LoginRequiredMixin, TemplateView):
#     template_name = 'home/authorized.html'
#     login_url = '/login'

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
