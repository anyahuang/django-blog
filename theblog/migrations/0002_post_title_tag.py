# Generated by Django 3.2.8 on 2021-10-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="An~yaaaaa's Blog!", max_length=255),
        ),
    ]