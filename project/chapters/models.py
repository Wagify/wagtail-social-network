from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import URLBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

from accounts.models import User
from .forms import GroupMembershipForm


# Create your models here.


class GroupsIndexPage(Page):
    introduction = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]

    subpage_types = []

    max_count = 1

    additional_context = "groups"
    context_order = ("title",)

    class Meta:
        abstract = True

    def get_context(self, request):
        """
        return a Queryset of Groups
        """
        context = super().get_context(request)
        context[self.additional_context] = (
            self.allowed_subpage_models()[0]
            .objects.child_of(self)
            .live()
            .order_by(*self.context_order)
        )
        return context


class ChaptersIndexPage(GroupsIndexPage):
    subpage_types = ["chapters.Chapter"]
    additional_context = "chapters"
    context_order = ("region", "title")


class Group(Page):
    introduction = RichTextField()

    links =  StreamField([
    ('social_media_link', URLBlock(required=False,form_classname="social media link")),
    ('website_link', URLBlock(required=False,form_classname="website link"))
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        FieldPanel("links", classname="full")
    ]

    members = models.ManyToManyField(User, blank=True)

    class Meta:
        abstract = True

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Check whether request user is a member of current group
        context["member"] = request.user in self.members.all()

        return context

    def serve(self, request, *args, **kwargs):
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = GroupMembershipForm(request.POST)

            if form.is_valid():
                membership_action = form.cleaned_data.get("membership_action")
                if membership_action == "join":
                    self.members.add(request.user)
                elif membership_action == "leave":
                    self.members.remove(request.user)

        return super().serve(request, *args, **kwargs)


class Chapter(Group):
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

    content_panels = Group.content_panels + [
        FieldPanel("region"),
    ]

    parent_page_types = [
        "chapters.ChaptersIndexPage",
    ]
    subpage_types = []
