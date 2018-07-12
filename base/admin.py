from django.contrib import admin

from . import models


class MessagesInline(admin.TabularInline):
    readonly_fields = ('text', 'create_date', 'channel', 'sender')
    extra = 0
    model = models.Message


class ChannelAdmin(admin.ModelAdmin):

    list_display = ('title',  'create_date', 'modify_date',)
    inlines = (MessagesInline,)


admin.site.register(models.Channel, ChannelAdmin)