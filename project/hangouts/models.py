from django.db import models
from django.shortcuts import redirect
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItemBase
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.blocks import URLBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

def topics_with_url(topics,parent_url):
    for topic in topics:
        topic.url = "/" + "/".join(
            s.strip("/") for s in [parent_url, "topics", topic.slug]
        )
    return topics

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

    @property
    def get_topics(self):
        topics = self.topics.all()

        return topics_with_url(topics,self.get_parent().url)


class HangoutsIndexPage(RoutablePageMixin, Page):
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
        context["hangouts"] = self.get_hangouts()
        return context

    @route(r"^topics/$", name="topic_archive")
    @route(r"^topics/([\w-]+)/$", name="topic_archive")
    def tag_archive(self, request, topic=None):

        try:
            topic = Tag.objects.get(slug=topic)
        except Tag.DoesNotExist:
            if topic:
                msg = 'There are no hangouts in the topic "{}"'.format(topic)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        hangouts = self.get_hangouts(topic=topic)

        return self.render(
            request, context_overrides={"topic": topic, "hangouts": hangouts}
        )

    def get_hangouts(self, topic=None):
        hangouts = (
            Hangout.objects.live().descendant_of(self).order_by("-last_published_at")
        )
        if topic:
            hangouts = hangouts.filter(topics=topic)
        return hangouts

    def get_child_topics(self):
        topics = Tag.objects.filter(hangout__in=self.get_hangouts()).distinct()
        return topics_with_url(topics,self.url)
