

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('event_app.urls')),
    # path('account/', include('user_profile.urls')),

]
