

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from lemonApp import views

router = DefaultRouter(trailing_slash=True)
router.register('tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lemonapp/', include('lemonApp.urls')),
    path('lemonapp/booking/', include(router.urls)),
]
