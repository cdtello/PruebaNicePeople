from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EasyCook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.recetas.urls', namespace="recetas")),
    url(r'accounts/login/$',login,{'template_name':'index.html'},name='login'),

)
