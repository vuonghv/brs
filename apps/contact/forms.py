from django import forms
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    """docstring for ContactForm"""
    fullname = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    captcha = ReCaptchaField()
