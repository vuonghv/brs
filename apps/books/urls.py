from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(), name='index'),
	url(r'^(?P<slug>[\w-]+)/$', views.DetailView, name='detail'),
]
