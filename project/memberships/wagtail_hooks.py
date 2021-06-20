from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Membership


class MembershipModelAdmin(ModelAdmin):
    model = Membership
    menu_label = "Memberships"
    menu_icon = "user"
    menu_order = 201
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = ("chapter", "user", "status",)
    list_filter = ("status",)
    # TODO: determine how to search on user.username
    # FieldError: Cannot resolve keyword 'user.username' into field.
    # search_fields = ("user.username",)

modeladmin_register(MembershipModelAdmin)
