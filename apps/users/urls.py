from django.conf.urls import url

from apps.users import views


urlpatterns = [
        url(r'^signup/$', views.SignupUserView.as_view(), name='signup'),
        url(r'^login/$', views.LoginUserView.as_view(), name='login'),
        url(r'^logout/$', views.logout_user, name='logout'),
]
