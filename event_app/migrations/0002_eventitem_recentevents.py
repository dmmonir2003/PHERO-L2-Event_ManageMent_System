# Generated by Django 5.0.1 on 2024-02-23 06:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_image', models.URLField()),
                ('item_title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RecentEvents',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=150)),
                ('event_description', models.TextField()),
                ('event_images', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(), blank=True, null=True, size=None)),
            ],
        ),
    ]
