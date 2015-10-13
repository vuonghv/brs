from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^signup/$', views.SignupUserView.as_view(), name='signup'),
        url(r'^login/$', views.LoginUserView.as_view(), name='login'),
        url(r'^logout/$', views.logout_user, name='logout'),
        url(r'^follow/(?P<pk>[0-9]+)/$', views.follow_user, name='follow'),
        url(r'^unfollow/(?P<pk>[0-9]+)/$', views.unfollow_user, name='unfollow'),
        url(r'^(?P<pk>[0-9]+)/followers/$', views.ListFollowersView.as_view(), name='followers'),
        url(r'^(?P<pk>[0-9]+)/following/$', views.ListFollowingView.as_view(), name='following'),
]
