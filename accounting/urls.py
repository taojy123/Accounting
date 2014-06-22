from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    ('^$', index),
    ('^index/$', index),

    ('^add_account/$', add_account),
    ('^del_account/$', del_account),
    ('^update_account/$', update_account),

    ('^pay/$', pay),
    ('^unpaid/$', unpaid),
)
# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
