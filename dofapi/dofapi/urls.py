from django.conf.urls import patterns, include, url
from tastypie.api import Api
from apiapp.api import PublicacionResource

v1_api = Api(api_name='v1')
v1_api.register(PublicacionResource())

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dofapi.views.home', name='home'),
    # url(r'^dofapi/', include('dofapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))
)
