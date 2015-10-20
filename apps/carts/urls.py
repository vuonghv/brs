from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.ViewCart.as_view(), name='view'),
        url(r'^add/$', views.AddBookToCart.as_view(), name='add'),
        url(r'^remove/$', views.RemoveBookFromCart.as_view(), name='remove'),
        url(r'^update/$', views.UpdateBookToCart.as_view(), name='update'),
]
