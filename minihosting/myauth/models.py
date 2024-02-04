from django.db import models
from django.contrib.auth.models import User

def avatar_path(instance: "Profile", filename: str) -> str:
    return "images/user_{pk}/{filename}".format(
        pk=instance.user.pk,
        filename=filename
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=avatar_path,
        verbose_name='avatar'
    )

    class Meta:
        permissions = (("change_avatar", "can change avatar of profile"),)

    def __str__(self):
        return self.user.username

