from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.DetaiBookView.as_view(), name='detail'),
    url(r'^search/$', views.SearchBookView.as_view(), name='search'),
    url(r'^recommendations/$', views.RecommendationsBookView.as_view(), name='recommendations'),
]
