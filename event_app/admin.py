from django.contrib import admin
from .models import EventsCategories, Service, EventItem, RecentEvents
# Register your models here.


admin.site.register(Service)
admin.site.register(EventsCategories)

admin.site.register(EventItem)
admin.site.register(RecentEvents)
