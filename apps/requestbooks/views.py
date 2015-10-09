from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.conf import settings

from apps.requestbooks.models import RequestedBook


class LoginRequiredView(View):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ListRequests(LoginRequiredView, ListView):
    model = RequestedBook
    template_name = 'requestbooks/list.html'
