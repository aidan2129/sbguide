# Generated by Django 2.2 on 2019-04-28 12:11

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0004_deck_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]