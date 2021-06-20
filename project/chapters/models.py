from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

# Create your models here.
class Chapter(Page):
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
    ]