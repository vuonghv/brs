from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.DashboardAdmin.as_view(), name='dashboard'),
    url(r'^login/$', views.LoginAdmin.as_view(), name='login'),
    url(r'^logout/$', views.logout_admin, name='logout'),
]
