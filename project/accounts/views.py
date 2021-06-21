from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserViewSet

from .models import User

class UserChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = User
    page_title =  _("Choose a person")
    per_page = 10
    order_by = ("last_name", "first_name")
    fields = ("first_name", "last_name", "username",)
