import datetime

from django.db import models

from apps.accounts.models import UserAccount


class Publication(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Publication title')
    content = models.TextField(null=True, blank=True, verbose_name='Publication content')
    published_at = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now, verbose_name='Time created')

    publisher = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='Publication creator')

    def __str__(self):
        return f'{self.title}'
