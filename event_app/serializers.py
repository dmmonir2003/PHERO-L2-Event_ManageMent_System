
from .models import Service
from .models import Service, EventsCategories, EventItem, RecentEvents
from rest_framework import serializers


class EventsCategoriesSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = EventsCategories
        fields = ['name', 'slug']


class ServiceSerializer(serializers.ModelSerializer):
    category = EventsCategoriesSerializer()
    services = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Service
        fields = ['service_id', 'title', 'services',
                  'image_url', 'description', 'category']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance, _ = EventsCategories.objects.get_or_create(
            **category_data)
        service = Service.objects.create(
            category=category_instance, **validated_data)
        return service


class ServiceUpdateSerializer(serializers.ModelSerializer):
    category = serializers.DictField(write_only=True, required=False)

    class Meta:
        model = Service
        fields = ['service_id', 'title', 'services',
                  'image_url', 'description', 'category']

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)

        if category_data:
            category_name = category_data.get('name')
            category_instance, _ = EventsCategories.objects.get_or_create(
                name=category_name)
            instance.category = category_instance

        instance.title = validated_data.get('title', instance.title)
        instance.services = validated_data.get('services', instance.services)
        instance.image_url = validated_data.get(
            'image_url', instance.image_url)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_instance = instance.category
        if category_instance:
            representation['category'] = {'name': category_instance.name}
        return representation

#  event Item section


class EventItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventItem
        fields = ['item_id', 'item_image', 'item_title']


class EventItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventItem
        fields = ['item_id', 'item_image', 'item_title']


class RecentEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentEvents
        fields = ['event_id', 'event_title',
                  'event_description', 'event_images']
