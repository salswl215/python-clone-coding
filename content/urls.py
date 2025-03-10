from django.urls import path
from .views import UploadFeed, Profile


urlpatterns = [
    path('upload', UploadFeed.as_view(), name = 'upload'),
    path('profile', Profile.as_view(), name = 'upload')
]

