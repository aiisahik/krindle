from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import LoginView,LogoutView


urlpatterns = patterns('',
	url(r'^login/', LoginView.as_view()),
	url(r'^logout/', LogoutView.as_view()),
)