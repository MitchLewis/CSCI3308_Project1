from django.conf.urls import patterns, url
from matchApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^classpage/$', views.classpage, name='classpage'))