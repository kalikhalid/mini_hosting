from django.urls import path, include
from .views import (
    VideoCreateView,
    VideoListView,
)
app_name = 'hosting'

urlpatterns = [
    path('', VideoListView.as_view(), name='index'),
    # path('video/<pk>', views.video, name='video'),
    path('upload', VideoCreateView.as_view(), name='upload-video'),
]