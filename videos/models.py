from djongo import models


class Video(models.Model):
    title = models.CharField(max_length=200, unique=False)
    description = models.TextField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
