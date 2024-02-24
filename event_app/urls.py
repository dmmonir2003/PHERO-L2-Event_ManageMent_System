from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('create-service', views.CreateServiceViewSet,
                basename='create-service')
router.register('service-list', views.AllServices,
                basename='service-list')
router.register('categories', views.EventsCategoriesViewSet,
                basename='categories')

router.register('service-list-by-category',
                views.ServiceListByCategoryAPIView, basename='service-list-by-category')
router.register('service-update', views.ServiceUpdateViewSet,
                basename='service-update')
router.register(r'service-delete', views.ServiceDeleteViewSet,
                basename='service-delete')
router.register('eventitem_create', views.EventItemCreateViewSet,
                basename='eventitem_create')
router.register('all_event_item', views.AllEventItemViewSet,
                basename='all_event_item')
router.register(r'event_update', views.EventItemUpdateViewSet,
                basename='event_update')
router.register(r'event_item-delete', views.EventItemDeleteViewSet,
                basename='event_item-delete')
router.register(r'recent-event', views.RecentEventViewSet,
                basename='recent-event')


urlpatterns = [
    path('', include(router.urls)),

]
