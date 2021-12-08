from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import URLBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page


class HangoutTag(TaggedItemBase):
    content_object = ParentalKey(
        "hangouts.Hangout", related_name="tagged_items", on_delete=models.CASCADE
    )


# Create your models here.
class Hangout(Page):
    description = RichTextField()
    topics = ClusterTaggableManager(through=HangoutTag, blank=True)
    link = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
        FieldPanel("topics", classname="full"),
        FieldPanel("link", classname="full"),
    ]
    parent_page_types = [
        "hangouts.HangoutsIndexPage",
    ]
    subpage_types = []


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
