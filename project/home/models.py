from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    intro = models.CharField(max_length=250)
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]
