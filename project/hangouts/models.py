from django.db import models
from taggit.managers import TaggableManager
from wagtail.core.fields import RichTextField


# Create your models here.
class Hangout(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    topics = TaggableManager()
    url = models.URLField(blank=True, null=True)
