
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    
    path('secret/', views.secret, name='secret'),
    
    path('menu-api/', views.MenuItemsView.as_view(), name='menu_api'),
    path('menu-api/<int:pk>', views.MenuItemsDetailView.as_view(), name='menu_api_detail'),

    path('token/', obtain_auth_token)
]