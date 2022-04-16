from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add_video"),
    path('video_list', views.video_list, name="video_list"),
    path('video_details/<str:video_pk>', views.video_details, name="video_details")
]