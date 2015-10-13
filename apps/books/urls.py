from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$', views.DetaiBookView.as_view(), name='detail'),
    url(r'^search/$', views.SearchBookView.as_view(), name='search'),
    url(r'^recommendations/$', views.RecommendationsBookView.as_view(), name='recommendations'),
    url(r'^read/$', views.ReadBookView.as_view(), name='read'),
    url(r'^update-read/(?P<pk>[0-9]+)$', views.UpdateReadBookView.as_view(), name='update-read'),
    url(r'^history/(?P<username>[\w]+)$', views.ListHistoryBookView.as_view(), name='history'),
    url(r'^favorite/(?P<pk>[0-9]+)$', views.FavoriteBookView.as_view(), name='favorite'),
    url(r'^remove-favorite/(?P<pk>[0-9]+)$', views.RemoveFavoriteBookView.as_view(), name='remove-favorite'),
]
