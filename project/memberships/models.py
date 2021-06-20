from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

from instance_selector.edit_handlers import InstanceSelectorPanel

class Membership(models.Model):
    class MembershipStatusChoices(models.TextChoices):
        PENDING = "Pending", _("Pending")
        ACTIVE = "Active", _("Active")
        LAPSED = "Lapsed", _("Lapsed")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    chapter = models.ForeignKey(
        "chapters.Chapter",
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=32,
        choices=MembershipStatusChoices.choices,
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ["user", "chapter"]

    panels = [
        InstanceSelectorPanel("user"),
        PageChooserPanel("chapter"),
        FieldPanel("status"),
    ]

    def __str__(self):
        return f"{ self.user } - { self.chapter } ({ self.status })"