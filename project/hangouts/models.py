from django.db import models
from taggit.managers import TaggableManager
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class Hangout(Page):
    description = RichTextField()
    topics = TaggableManager()
    url = models.URLField(blank=True, null=True)


class HangoutsIndexPage(Page):
    introduction = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    parent_page_types = [
        "home.HomePage",
    ]

    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["hangouts"] = Hangout.objects.all()
        return context
