from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from models import UserProfile

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


class ProfileView(DetailView):
    # model = UserProfile
    context_object_name = 'user_profile'
    def get_object(self):
        if self.request.user:
            return UserProfile.objects.get(user=self.request.user)
        else:
            return HttpResponseRedirect("/match/")

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

class EditProfileView(ProfileView, TemplateView):
    template_name="account/editProfile.html"

    def get_context_data(self, **kwargs):
        context = super(EditProfileView, self).get_context_data(**kwargs)
        return context

