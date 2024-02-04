from django.db import models
import hashlib
from django.contrib.auth.models import User


def make_hash(last_hash: str) -> str:
    string = hashlib.md5(last_hash.encode()).hexdigest()[:10]
    return string


def get_video_file_name(instance: "Video", filename: str) -> str:
    return f"videos/video_{instance.user.username}/{instance.hash}_{filename}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to=get_video_file_name, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos', null=False, blank=False)
    hash = models.CharField(max_length=10, primary_key=True)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
