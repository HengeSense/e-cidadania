from django.conf.urls.defaults import *

urlpatterns = patterns('e_cidadania.apps.third_party.smart_selects.views',
    url(r'^all/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<field>[\w\-]+)/(?P<value>[\w\-]+)/$', 'filterchain_all', name='chained_filter_all'),
    url(r'^filter/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<field>[\w\-]+)/(?P<value>[\w\-]+)/$', 'filterchain', name='chained_filter'),
    url(r'^filter/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<manager>[\w\-]+)/(?P<field>[\w\-]+)/(?P<value>[\w\-]+)/$', 'filterchain', name='chained_filter'),
)
