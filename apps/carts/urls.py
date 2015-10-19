from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.ViewCart.as_view(), name='view'),
        url(r'^add/$', views.AddBookToCart.as_view(), name='add'),
]
