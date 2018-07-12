
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from . import receivers

User = 'auth.User'


class ActiveChannelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()


class Channel(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    topic = models.CharField(_('Topic'), max_length=256, null=True, blank=True)
    create_date = models.DateTimeField(_('Date created'), auto_now_add=True)
    modify_date = models.DateTimeField(_('Date modified'), auto_now=True)
    objects = models.Manager()
    active = ActiveChannelManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = _('Channel')
        verbose_name_plural = _('Channels')


class Message(models.Model):
    text = models.TextField(_('Text'), max_length=1024)
    create_date = models.DateTimeField(_('Date created'), auto_now_add=True,
                                       db_index=True)
    channel = models.ForeignKey(Channel, verbose_name=_('Channel'), on_delete=models.DO_NOTHING)
    sender = models.ForeignKey(User, verbose_name='Sender', on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['create_date']
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')


post_save.connect(receivers.create_auth_token, sender=User)
