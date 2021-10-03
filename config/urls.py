from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include('user.urls')),
    path("", include('task_tracker.urls'))
]

urlpatterns += staticfiles_urlpatterns()