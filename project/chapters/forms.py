from django import forms


class GroupMembershipForm(forms.Form):
    MEMBERSHIP_ACTION_CHOICES = [("join", "Join"), ("leave", "Leave")]

    membership_action = forms.ChoiceField(
        label="Membership action", choices=MEMBERSHIP_ACTION_CHOICES
    )
