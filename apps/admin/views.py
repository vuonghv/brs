from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.admin.forms import AdminAuthenticationForm
from django.views.generic import FormView, View, DetailView, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class LoginAdmin(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.is_staff:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        admin = form.get_user()
        login(self.request, admin)
        return super().form_valid(form)


def logout_admin(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('admin:login'))


class AdminRequiredView(View):
    
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DashboardAdmin(AdminRequiredView, TemplateView):
    template_name = 'admin/dashboard.html'
