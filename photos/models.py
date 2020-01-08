from django.db import models
from django.contrib.auth.models import User
from photos.settings import LICENSES
from photos.validators import badwords_detector


PUBLIC = "PUB"
PRIVATE = "PRI"

VISIBILITY = (
    (PUBLIC, "Pública"),
    (PRIVATE, "Privada")
)


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, default="", validators=[badwords_detector])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __str__(self):
        return self.name
