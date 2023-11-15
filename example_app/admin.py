from django.contrib import admin

from .models import TextID


class TextAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'text')


admin.site.register(TextID, TextAdmin)
