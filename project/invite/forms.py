from django import forms
from home.models import FriendInvitation


class FriendInvitationForm(forms.ModelForm):
    class Meta:
        model = FriendInvitation
        fields = ['email']
