
from django.urls import path, include, re_path

from . import  views

urlpatterns = [
    path('', views.home),
    re_path(r'^news(?:/.*)?$', views.news),
    re_path(r'^management(?:/.*)?$', views.management),
    re_path(r'^facts(?:/.*)?$', views.facts),
    re_path(r'^contacts(?:/.*)?$', views.contacts),
    re_path(r'^history/?$', views.history),
    re_path(r'^history/people/?$', views.history_people),
    re_path(r'^history/photos/?$', views.history_photos),
]
