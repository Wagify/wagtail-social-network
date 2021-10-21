from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from invites.models import InviteFriendsPage


class HomePage(Page):
    intro = models.CharField(max_length=250, default="Introduction Line")
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('content'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['invite_friends_page'] = InviteFriendsPage.objects.get()
        print(context)
        return context
