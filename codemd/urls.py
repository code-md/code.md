from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cruiser.views.index', name='index'),
    # url(r'^coderr/', include('coderr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
