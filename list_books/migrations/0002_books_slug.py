# Generated by Django 4.1.6 on 2023-02-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
