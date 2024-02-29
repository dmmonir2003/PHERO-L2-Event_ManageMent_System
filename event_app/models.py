from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver


class EventsCategories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(
        EventsCategories, on_delete=models.CASCADE, related_name='category_title')
    title = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField()
    services = ArrayField(models.CharField(
        max_length=200), blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class EventItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_image = models.URLField()
    item_title = models.CharField(max_length=150)


class RecentEvents(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=150)
    event_description = models.TextField()
    event_images = ArrayField(models.URLField(
        max_length=200), blank=True, null=True)
