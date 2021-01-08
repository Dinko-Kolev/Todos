from app import views

from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
