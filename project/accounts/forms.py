from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    first_name = forms.CharField(required=False, label=_("First name"))
    last_name = forms.CharField(required=False, label=_("Last name"))


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=False, label=_("First name"))
    last_name = forms.CharField(required=False, label=_("Last name"))
