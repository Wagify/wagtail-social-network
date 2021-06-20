from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


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

# Create your models here.
class Chapter(Page):
    class RegionChoices(models.TextChoices):
        AFRICA = "Africa", _("Africa")
        ANTARCTICA = "Antarctica", _("Antarctica")
        ASIA = "Asia", _("Asia")
        AUSTRALIA = "Australia", _("Australia")
        EUROPE = "Europe", _("Europe")
        NORTH_AMERICA = "North America", _("North America")
        SOUTH_AMERICA = "South America", _("South America")

    introduction = RichTextField()
    region = models.CharField(
        max_length=32,
        choices=RegionChoices.choices,
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        FieldPanel("region"),
    ]

    parent_page_types = [
        "chapters.ChaptersIndexPage",
    ]
    subpage_types = []