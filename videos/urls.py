from django.urls import path
from .views import VideoManagemntViewSet
from django.urls import include


from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'video_managemnt', VideoManagemntViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]