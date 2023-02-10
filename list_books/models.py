import datetime

from django.db import models
from django.shortcuts import reverse
from pytils.translit import slugify

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)
    time_delta = models.IntegerField(null=True)
    slug = models.SlugField(default='', null=False)

    def get_url(self):
        return reverse('book-info', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.title)}-{slugify(self.author)}'
        if self.time_delta is None:
            if self.date_start and self.date_end:
                self.time_delta = (self.date_end - self.date_start).days
            elif self.date_start and not self.date_end:
                self.time_delta = (datetime.datetime.now() - self.date_start.replace(tzinfo=None)).days
        super().save(*args, **kwargs)
