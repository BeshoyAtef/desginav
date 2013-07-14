from django.conf.urls import patterns, include, url
from designav_www.views import*

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'designav_www.views.home'),
    url(r'^getProjects/$', 'designav_www.views.view_all_projects'),
    url(r'^getTeamMembers/$', 'designav_www.views.view_all_members'),
    url(r'^getNews/$', 'designav_www.views.view_all_news'),
    url(r'^getProject/$', 'designav_www.views.view_project'),
    # url(r'^designav/', include('designav.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
