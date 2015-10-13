from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
        UserCreationForm,
        AuthenticationForm,
)
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.conf import settings
from django.apps import apps as django_apps
from django.contrib import messages
from django.shortcuts import get_object_or_404

from apps.core.views import BaseView, LoginRequiredMixin
from apps.users.models import FollowShip, UserProfile


class SignupUserView(BaseView, CreateView):
    model = django_apps.get_model(settings.AUTH_USER_MODEL)
    form_class = UserCreationForm
    template_name = 'users/signup.html'

    def get_success_url(self):
        return reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(SignupUserView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Signup - Book Review'
            }
        }
        context.update(info)
        return context

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "You've signed up successfully,\
                            You can log in now.")
        return HttpResponseRedirect(self.get_success_url())

class LoginUserView(BaseView, FormView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', False)
        info = {
            'info': {
                'title': 'Login - Book Review'
            }
        }
        context.update(info)
        return context

    def get_success_url(self):
        nextlink = self.request.POST.get('next', False)
        if nextlink:
            return nextlink
        return reverse_lazy('books:index')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('books:index'))

@login_required
def follow_user(request, pk):
    url = reverse_lazy('users:following', kwargs={'pk': request.user.pk})
    if request.method == 'POST':
        followee = get_object_or_404(UserProfile, pk=pk)
        follower = request.user.profile
        if followee == follower:
            return HttpResponseRedirect(url)
        FollowShip.objects.get_or_create(follower=follower, followee=followee)

    return HttpResponseRedirect(url)

@login_required
def unfollow_user(request, pk):
    url = reverse_lazy('users:following', kwargs={'pk': request.user.pk})
    if request.method == 'POST':
        followee = get_object_or_404(UserProfile, pk=pk)
        follower = request.user.profile
        relation = get_object_or_404(FollowShip,
                        follower=follower, followee=followee)
        relation.delete()
    
    return HttpResponseRedirect(url)


class ListFollowersView(LoginRequiredMixin, SingleObjectMixin, BaseView, ListView):
    template_name = 'users/followers.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=UserProfile.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.followers.select_related('user').all()


class ListFollowingView(LoginRequiredMixin, SingleObjectMixin, BaseView, ListView):
    template_name = 'users/following.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=UserProfile.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.following.select_related('user').all()
