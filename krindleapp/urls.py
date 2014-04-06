from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'krindleapp.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^account/', include('account.urls')),
    url(r'^login/', TemplateView.as_view(template_name="login.html")),

    url(r'^admin/', include(admin.site.urls)),
)
