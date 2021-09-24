from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from invites.models import InviteFriendsPage


class HomePage(Page):
    intro = models.CharField(max_length=250,default="Introduction Line")
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    def get_context(self,request):
        context = super().get_context(request)
        context['invite_friends'] = self.get_children().type(InviteFriendsPage)
        print(context)
        return context
