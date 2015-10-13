from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
                        {'next_page': '/admin/login/'}, name='logout'),

    #############################################################
    #############################################################
    #############################################################
    # Url category
    url(r'^category/$', views.CategoryView.as_view(), name='list_category'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='create_category'),
    url(r'^category/update/(?P<pk>[0-9]+)/$', views.CategoryUpdateView.as_view(), 
    																name='update_category'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$', views.CategoryDeleteView.as_view(), 
																	name='delete_category'),

	#############################################################
    #############################################################
    #############################################################
    # Url book
    url(r'^book/$', views.BookView.as_view(), name='list_book'),
    url(r'^book/create/$', views.BookCreateView.as_view(), name='create_book'),
    url(r'^book/update/(?P<pk>[0-9]+)/$', views.BookUpdateView.as_view(), name='update_book'),
    url(r'^book/delete/(?P<pk>[0-9]+)/$', views.BookDeleteView.as_view(), name='delete_book'),

    #############################################################
    #############################################################
    #############################################################
    # Url requested book
    url(r'^request/$', views.RequestedBookView.as_view(), name='list_requested_book'),

    url(r'^request/update/(?P<pk>[0-9]+)/$',
        views.RequestedBookUpdateView.as_view(),
        name='update_requested_book'),

    url(r'^request/delete/(?P<pk>[0-9]+)/$',
        views.RequestedBookDeleteView.as_view(),
        name='delete_requested_book'),

    #############################################################
    #############################################################
    #############################################################
    # Url user
    url(r'^user/$', views.UserProfileView.as_view(), name='list_user'),

    url(r'^user/delete/(?P<pk>[0-9]+)/$',
        views.UserProfileDeleteView.as_view(),
        name='delete_user'),
]
