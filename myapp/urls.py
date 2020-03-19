from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('files/count/', views.count, name='count'),

    path('files/', views.file_list, name='file_list'),
    path('upload/', views.upload, name='upload')
]
