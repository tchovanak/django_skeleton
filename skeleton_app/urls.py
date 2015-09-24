from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
import dbindexer

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url('^$', direct_to_template, {'template': 'home.html'}),
    url('^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'skeletonapp.views.home', name='home'),
    # url(r'^skeletonapp/', include('skeletonapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
