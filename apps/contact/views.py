from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from django.core.mail import send_mail

from apps.core.views import BaseView
from . import forms

class ContactView(BaseView, FormView):
    form_class = forms.ContactForm
    """docstring for ContactView"""
    template_name = "contact/index.html"

    def get_success_url(self):
        return reverse_lazy("contact:index")

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Contact - Book Review System',
            }            
        }
        context.update(info)
        return context

    def form_valid(self, form):
        fullname = form.cleaned_data['fullname']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        info = {
            'fullname': fullname,
            'email': email,
            'message': message
        }
        self.mail(info)
        messages.success(self.request,
                    "Sent email contact success !",
                    extra_tags='contact-message')
        return super(ContactView, self).form_valid(form)

    def mail(self, info):
        send_mail(info['fullname'], info['message'], info['email'], 
                        ['brs.framgia@gmail.com'], fail_silently=False)