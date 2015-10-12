from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.ListRequestsView.as_view(), name='index'),
        url(r'^new/$', views.CreateRequestView.as_view(), name='create'),
        url(r'^(?P<pk>[0-9]+)/$', views.DetailRequestView.as_view(), name='detail'),
        url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateRequestView.as_view(), name='update'),
        url(r'^(?P<pk>[0-9]+)/cancel/$', views.CancelRequestView.as_view(), name='cancel'),
]
