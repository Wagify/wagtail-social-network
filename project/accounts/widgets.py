from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from generic_chooser.widgets import AdminChooser

from  .models import User


class UserChooser(AdminChooser):
    choose_one_text = _("Choose a person")
    choose_another_text = _("Choose another person")
    link_to_chosen_text = _("Edit this person")
    model = User
    choose_modal_url_name = "user_chooser:choose"
