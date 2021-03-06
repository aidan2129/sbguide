# Generated by Django 2.2 on 2019-04-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('set_code', models.CharField(max_length=10)),
                ('image_link', models.URLField()),
                ('mana_cost', models.CharField(max_length=10)),
                ('standard_legal', models.BooleanField()),
                ('modern_legal', models.BooleanField()),
            ],
        ),
    ]
