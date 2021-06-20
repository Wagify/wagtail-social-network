from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Chapter


class ChapterAdmin(ModelAdmin):
    model = Chapter
    menu_label = "Chapters"
    menu_icon = "group"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("region", "title",)
    list_filter = ("region",)
    search_fields = ("title",)

modeladmin_register(ChapterAdmin)
