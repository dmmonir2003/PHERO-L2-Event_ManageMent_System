from rest_framework import viewsets
from .serializers import EventsCategoriesSerializer, ServiceUpdateSerializer, ServiceSerializer, EventItemSerializer,  RecentEventsSerializer
from .models import EventsCategories, Service, EventItem, RecentEvents
from rest_framework import status
from rest_framework.response import Response

from django_filters import FilterSet
from rest_framework import status
from rest_framework.viewsets import ViewSet


import logging
from django_filters.rest_framework import DjangoFilterBackend


logger = logging.getLogger(__name__)


# categories get request
class EventsCategoriesViewSet(viewsets.ModelViewSet):
    queryset = EventsCategories.objects.all()
    serializer_class = EventsCategoriesSerializer
    lookup_field = 'slug'


class AllServices(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# create event


class CreateServiceViewSet(ViewSet):
    def create(self, request):
        service_serializer = ServiceSerializer(data=request.data)
        if service_serializer.is_valid():
            service_serializer.save()
            return Response(service_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Validation Error: {service_serializer.errors}")
            return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# custom filter class
class ServiceFilter(FilterSet):
    class Meta:
        model = Service
        fields = {
            'category__slug': ['exact'],
        }


class ServiceListByCategoryAPIView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ServiceFilter


class ServiceUpdateViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceUpdateSerializer

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        print(request.data)
        if serializer.is_valid():

            category_data = request.data.get('category', None)
            if category_data and isinstance(category_data, dict):

                category_name = category_data.get('name')
                category_instance, _ = EventsCategories.objects.get_or_create(
                    name=category_name)
                instance.category = category_instance

            serializer.save()

            updated_instance = self.get_object()
            response_serializer = self.get_serializer(updated_instance)
            return Response(response_serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDeleteViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def destroy(self, request, pk=None):
        try:
            service = self.get_queryset().get(pk=pk)
            service.delete()
            return Response({"message": "Service deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Service.DoesNotExist:
            return Response({"error": "Service does not exist"}, status=status.HTTP_404_NOT_FOUND)


class EventItemCreateViewSet(viewsets.ModelViewSet):
    queryset = EventItem.objects.all()
    serializer_class = EventItemSerializer


class EventItemUpdateViewSet(viewsets.ModelViewSet):
    queryset = EventItem.objects.all()
    serializer_class = EventItemSerializer


class AllEventItemViewSet(viewsets.ModelViewSet):
    queryset = EventItem.objects.all()
    serializer_class = EventItemSerializer


class EventItemDeleteViewSet(viewsets.ModelViewSet):
    queryset = EventItem.objects.all()
    serializer_class = EventItemSerializer

    def destroy(self, request, pk=None):
        try:
            event_item = self.get_queryset().get(pk=pk)
            event_item.delete()
            return Response({"message": "event item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except EventItem.DoesNotExist:
            return Response({"error": "event item does not exist"}, status=status.HTTP_404_NOT_FOUND)


class RecentEventViewSet(viewsets.ModelViewSet):
    queryset = RecentEvents.objects.all()
    serializer_class = RecentEventsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
