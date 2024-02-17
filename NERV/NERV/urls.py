from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.pyti')),
    path('admin/', admin.site.urls)
]




