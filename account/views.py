from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from models import UserProfile, UserProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class EditProfileFormView(SingleObjectMixin, FormView):
    template_name="account/editProfile.html"
    form_class = UserProfileForm
    model = UserProfile
    success_url = "/account/edit/"

    @login_required
    def get_object(self):
        if self.request.user.is_authenticated():
            return UserProfile.objects.get(user=self.request.user)
        else: 
            return None
    
    @login_required    
    def dispatch(self, request, *args, **kwargs):
        # self.pk = kwargs.get('pk')
        self.object = self.get_object()
        return super(EditProfileFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print form
        return super(EditProfileFormView, self).form_valid(form)

class ProfileUpdateFormView(UpdateView):
    template_name_suffix = '_update'
    model = UserProfile
    fields = ['gender','hair_color']
    success_url = "/account/edit/"
    def get_object(self, queryset=None):
        obj = UserProfile.objects.get(user_id=self.request.user.id)
        return obj


 