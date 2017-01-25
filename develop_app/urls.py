from django.conf.urls import include, url
from develop_app.views import *

urlpatterns = [
    url(r'^login/$',login,name="login"),
    url(r'^logout/$',logout,name="logout"),
    url(r'^$',index,name="index"),
    url(r'^idc/$', idc,name='idc'),
    url(r'^addidc/$',addidc,name='addidc'),
    url(r'^deleteidc/$',deleteidc,name='deleteidc'),
    url(r'^editidc/$',editidc,name='editidc'),
    url(r'^updateidc/$',updateidc,name='updateidc'),
    url(r'^server/$', server,name='server'),
    url(r'^addserver/$', addserver,name='addserver'),
    url(r'^delserver/$', delserver,name='delserver'),
    url(r'^editserver/$',editserver,name='editserver'),
    url(r'^updateserver/$',updateserver,name='updateserver'),
]
