# Generated by Django 2.2 on 2019-04-28 12:16

import autoslug.fields
from django.db import migrations
import sideboards.models


class Migration(migrations.Migration):

    dependencies = [
        ('sideboards', '0002_sideboard_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sideboard',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=sideboards.models.get_slug),
        ),
    ]
