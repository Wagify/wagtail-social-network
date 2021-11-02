from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock, TextBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

from accounts.models import User


# Create your models here.
class ChaptersIndexPage(Page):
    introduction = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]
    subpage_types = ["chapters.Chapter"]

    max_count = 1

    def get_context(self, request):
        """
        return a Queryset of Chapters
        """
        context = super().get_context(request)
        context["chapters"] = (
            Chapter.objects.child_of(self).live().order_by("region", "title")
        )
        return context


class Groups(Page):
    introduction = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
    ]

    members = models.ManyToManyField(User, blank=True)

    class Meta:
        abstract = True

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        '''
        If user is a member display the greyed out button using
        the "context.member" variable, else display blue button
        for joining group
        '''
        if request.user in self.members.all():
            context["member"] = True
        else:
            context["member"] = False
        return context

    def serve(self, request, *args, **kwargs):
        # If query argument "join" is passed as true then add member
        if request.GET.get("join", "False").lower() == "true":
            # Later on can add code to get admin approval to join group --------
            self.members.add(request.user)

        # If query argument "leave" is passed as true then remove member
        if request.GET.get("leave", "False").lower() == "true":
            self.members.remove(request.user)

        return super().serve(request, *args, **kwargs)


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
