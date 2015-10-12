from django.contrib.auth.decorators import login_required
from django.views.generic import (
        DetailView, ListView, FormView, View, TemplateView
)
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.conf import settings

from apps.requestbooks.models import RequestedBook
from apps.categories.models import Category


class LoginRequiredMixin(object):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ListRequestsView(LoginRequiredMixin, ListView):
    model = RequestedBook
    template_name = 'requestbooks/list.html'

    def get_queryset(self):
        return self.model.objects.filter(
                            user_profile=self.request.user.profile
                            ).order_by('-requested_time')


class CreateRequestView(LoginRequiredMixin, CreateView):
    model = RequestedBook
    template_name = 'requestbooks/new.html'
    fields = ['title', 'description', 'categories']

    def get_success_url(self):
        return reverse_lazy('requests:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user_profile = self.request.user.profile
        return super().form_valid(form)


class DetailRequestView(LoginRequiredMixin, DetailView):
    model = RequestedBook
    template_name = 'requestbooks/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.object.categories.all()
        return context


class CancelRequestView(SingleObjectMixin, TemplateView):
    model = RequestedBook
    template_name = 'requestbooks/cancel.html'

    def get_success_url(self):
        return reverse_lazy('requests:detail', kwargs={'pk': self.object.pk})

    def handle_owner_permission(self):
        self.object = self.get_object()
        if self.object.user_profile != self.request.user.profile:
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        self.handle_owner_permission()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.handle_owner_permission()
        if (self.object.status == RequestedBook.APPROVED or
            self.object.status == RequestedBook.DISAPPROVED):
            raise PermissionDenied

        self.object.status = RequestedBook.CANCELED
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateRequestView(UpdateView):
    model = RequestedBook
    template_name = 'requestbooks/update.html'
    fields = ['title', 'description', 'categories']

    def get_success_url(self):
        return reverse_lazy('requests:detail', kwargs={'pk': self.object.pk})

    def handle_owner_permission(self):
        self.object = self.get_object()
        if self.object.user_profile != self.request.user.profile:
            raise PermissionDenied

    def get(self, request, *args, **kwargs):
        self.handle_owner_permission()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.handle_owner_permission()
        if (self.object.status == RequestedBook.APPROVED or
            self.object.status == RequestedBook.DISAPPROVED):
            raise PermissionDenied
        return super().post(request, *args, **kwargs)
