from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$', views.CommentReviewView.as_view(), name='create'),
    url(r'(?P<pk>[0-9]+)/delete/$', views.CommentDeleteView.as_view(), name='delete'),
    url(r'(?P<pk>[0-9]+)/edit/$', views.CommentUpdateView.as_view(), name='update'),
]
