# Generated by Django 2.2 on 2019-05-05 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('decks', '0005_auto_20190428_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deck_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]