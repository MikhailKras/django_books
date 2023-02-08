from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)

    # def __str__(self):
    #     if self.date_start is None and self.date_end is None:
    #         return f'{self.title}, {self.author}'
    #     elif self.date_end is None:
    #         return f'{self.title}, {self.author}, {self.date_start.strftime("%d.%m.%Y")}'
    #     return f'{self.title}, {self.author}, {self.date_start.strftime("%d.%m.%Y")}-{self.date_end.strftime("%d.%m.%Y")}'
