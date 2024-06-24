from .models import Video
from .serializers import VideoSerializer
from rest_framework.viewsets import ModelViewSet


class VideoManagemntViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
