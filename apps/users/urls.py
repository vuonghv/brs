from django.conf.urls import url

from apps.users import views


urlpatterns = [
        url(r'^signup/$', views.SignupUser.as_view(), name='signup'),
        url(r'^login/$', views.LoginUser.as_view(), name='login'),
        url(r'^logout/$', views.logout_user, name='logout'),
]
