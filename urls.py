"""
URLs for Openstack Dashboard Iframer Module.
"""


from django.conf.urls.defaults import *
from django.conf import settings


SYSPANEL = r'^syspanel/nixon/%s$'
DASH = r'^dash/nixon/%s$'


urlpatterns = patterns('nixon.views',
    url(SYSPANEL % 'munin', 'munin', name='os_dash_nixon_munin'),
)
