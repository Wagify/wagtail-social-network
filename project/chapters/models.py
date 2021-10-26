from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock, TextBlock
from wagtail.admin.edit_handlers import StreamFieldPanel


# Create your models here.
class ChaptersIndexPage(Page):
    introduction = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]
    subpage_types = [
        "chapters.Chapter"
    ]

    max_count = 1

    def get_context(self, request):
        """
        return a Queryset of Chapters
        """
        context = super().get_context(request)
        context['chapters'] = Chapter.objects.child_of(self).live()
        return context


class Groups(Page):
    body = StreamField([
        ("introduction",RichTextBlock(required=False)),
        ("description",TextBlock(required=False))
        ])

    content_panels = Page.content_panels + [
        StreamFieldPanel("body", classname="full"),
    ]

    class Meta:
        abstract=True

class Chapter(Groups):
    class RegionChoices(models.TextChoices):
        AFRICA = "Africa", _("Africa")
        ANTARCTICA = "Antarctica", _("Antarctica")
        ASIA = "Asia", _("Asia")
        AUSTRALIA = "Australia", _("Australia")
        EUROPE = "Europe", _("Europe")
        NORTH_AMERICA = "North America", _("North America")
        SOUTH_AMERICA = "South America", _("South America")

    region = models.CharField(
        max_length=32,
        choices=RegionChoices.choices,
        null=True,
        blank=True,
    )

    content_panels = Groups.content_panels + [
        FieldPanel("region"),
    ]

    parent_page_types = [
        "chapters.ChaptersIndexPage",
    ]
    subpage_types = []
