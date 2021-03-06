from django.conf.urls import url
from profiles.models import Profile

from django.shortcuts import render
from . import views

from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

import django_tables2 as tables


class SimpleTable(tables.Table):
    class Meta:
        model = Profile


def simple_list(request):
    queryset = Profile.objects.all()
    table = SimpleTable(queryset)
    return render(request, 'simple_list.html', {'table': table})


urlpatterns = [
    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^profiles/(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
    # example for show data in tabular form using table lib
    url(r'^usertype1/$', simple_list),
    url(r'^usertype/$', views.UserTypeList.as_view()),
    url(r'^usertype/(?P<pk>[0-9]+)/$', views.UserTypeDetail.as_view()),
]
