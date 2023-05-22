""" Notes admin """

from django.contrib import admin

from .import models


class NotesAdmin(admin.ModelAdmin):

    """ Notes from Django admin """

    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
