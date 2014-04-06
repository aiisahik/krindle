from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect

class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username and password: 
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/match/")
                else:
                    return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
        else: 
            return HttpResponseRedirect("/")

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect("/")
        # Redirect to a success page.