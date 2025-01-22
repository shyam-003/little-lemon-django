
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('secret/', views.secret, name='secret'),
    
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.MenuItemsDetailView.as_view(), name='menu_detail'),

    path('token/', obtain_auth_token)
]