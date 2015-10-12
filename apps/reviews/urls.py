from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.CreateReviewView.as_view(), name='create'),
]
