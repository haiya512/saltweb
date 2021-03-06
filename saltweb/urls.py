#!/usr/bin/env python
#coding=utf-8
#author: hhr
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from saltweb.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'saltweb.views.home', name='home'),
    # url(r'^saltweb/', include('saltweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^salt/admin/', include(admin.site.urls)),
    url(r'^salt/$', index ,name='index'),
    url(r'^salt/account_login/$', account_login ,name='account_login'),
    url(r'^salt/monitor/$', monitor ,name='monitor'),
    url(r'^salt/monitor1/$', monitor1 ,name='monitor1'),
    url(r'^salt/urlmonitor/$', urlmonitor ,name='urlmonitor'),
    url(r'^salt/alarm/$', alarm ,name='alarm'),
    url(r'^salt/server/$', server ,name='server'),
    url(r'^salt/assets/$', assets ,name='assets'),
    url(r'^salt/minions/$', minions ,name='minions'),
    url(r'^salt/chagelog/$', chagelog ,name='chagelog'),
    url(r'^salt/login/$', login ,name='login'),
    url(r'^salt/logout/$', logout ,name='logout'),
    url(r'^salt/saltcmd/$', saltcmd ,name='saltcmd'),
    url(r'^salt/sshcmd/$', sshcmd ,name='sshcmd'),
    url(r'^salt/accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'index.html'}),
    url(r'^salt/test/$', testpage),
    url(r'^salt/ajax/$', ajax_test ,name='ajax'),
    url(r'^salt/upload/$', upload ,name='upload'),
    url(r'^salt/audit/$', audit ,name='audit'),
    url(r'^salt/syncfile/$', Syncfile ,name='syncfile'),
    url(r'^salt/memtest/$', memcached_test),
    url(r'^salt/sysuser/$', sysuser ,name='sysuser'),
    url(r'^salt/install/$', install ,name='install'),
    url(r'^salt/optlog/$', optlog ,name='optlog'),
    url(r'^salt/todo/$', todolist,name='todo'),
    url(r'^salt/todoadd/$', todoadd,name='add'),
    url(r'^salt/todofinish/(?P<id>\d+)/$', todofinish,name='finish'),
    url(r'^salt/todobackout/(?P<id>\d+)/$', todoback,name='backout'),
    url(r'^salt/todoupdate/(?P<id>\d+)/$', todoupdate,name='update'),
    url(r'^salt/tododelete/(?P<id>\d+)/$', tododelete,name='delete'),
    url(r'^salt/address/$', address,name='address'),
    url(r'^salt/msg/$', msg,name='msg'),
    url(r'^salt/readmsg/(?P<id>\d+)/$', readmsg,name='readmsg'),
    url(r'^salt/delmsg/(?P<id>\d+)/$', delmsg,name='delmsg'),
    url(r'^salt/urlupdate/(?P<id>\d+)/$', urlupdate,name='urlupdate'),
    url(r'^salt/urldel/(?P<id>\d+)/$', urldel,name='urldel'),
    url(r'^salt/groups/$', groups,name='groups'),
)
