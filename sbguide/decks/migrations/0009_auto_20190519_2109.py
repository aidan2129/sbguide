# Generated by Django 2.2 on 2019-05-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0008_auto_20190519_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='slug',
            field=models.SlugField(),
        ),
    ]
