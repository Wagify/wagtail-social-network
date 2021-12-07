from django.db import models
from taggit.managers import TaggableManager
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import URLBlock


# Create your models here.
class Hangout(Page):
    description = RichTextField()
    topics = TaggableManager()
    url = models.URLField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("description",classname="full"),
        FieldPanel("topics",classname="full"),
        FieldPanel("url",classname="full")
    ]
    parent_page_types = [
        "hangouts.HangoutsIndexPage",
    ]


class HangoutsIndexPage(Page):
    introduction = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]

    subpage_types = ["hangouts.Hangout"]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["hangouts"] = (
            self.allowed_subpage_models()[0]
            .objects.child_of(self)
            .live()
            .order_by("title")
        )
        return context
