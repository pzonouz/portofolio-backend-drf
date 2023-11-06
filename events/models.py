from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    video_link = models.TextField()

    def __str__(self) -> str:
        return self.name
