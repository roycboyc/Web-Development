from django.conf.urls import include, url
from django.contrib import admin
from Squawk import message
urlpatterns = [

    url(r'^$', views.index, name='index'),
    utl(r'^Squawk/(?P<id>\d+)/', views.Squawk_detail, name='Squawk_detail')
    url(r'^admin/$', include(admin.site.urls)),
]
