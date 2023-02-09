from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)

    def get_url(self):
        return reverse('book-info', args=[self.id])
