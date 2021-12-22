from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from invites.models import InviteFriendsPage
from chapters.models import ChaptersIndexPage

from django.utils.translation import gettext


class HomePage(Page):
    intro = models.CharField(max_length=250, default="Introduction Line")
    content = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ],
        blank=True,
    )
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
        StreamFieldPanel("content"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # Get Respective page objects in context for redirection and links
        try:
            context["invite_friends_page"] = InviteFriendsPage.objects.get()
        except ObjectDoesNotExist:
            context["invite_friends_page"] = None
        
        try:
            context["chapters_index_page"] = ChaptersIndexPage.objects.get()
        except ObjectDoesNotExist:
            context["chapters_index_page"] = None
        
        return context
