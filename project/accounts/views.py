from django.utils.translation import gettext_lazy as _

from generic_chooser.views import ModelChooserMixin, ModelChooserViewSet

from .models import User

# Custom user chooser mixin to allow searching
# non-indexed User model
# https://github.com/wagtail/wagtail-generic-chooser/issues/11#issuecomment-622032350
class UserChooserMixin(ModelChooserMixin):
    """Custom Mixin to enable searching of non-indexed taggit.Tag model."""

    @property
    def is_searchable(self):
        return True

    def get_object_list(self, search_term=None, **kwargs):
        object_list = self.get_unfiltered_object_list()

        if search_term:
            object_list = object_list.filter(username__icontains=search_term)
        
        return object_list


class UserChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = User
    chooser_mixin_class = UserChooserMixin
    page_title =  _("Choose a person")
    per_page = 10
    order_by = ("last_name", "first_name")
