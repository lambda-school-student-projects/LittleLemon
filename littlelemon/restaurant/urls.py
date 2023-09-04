from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]
