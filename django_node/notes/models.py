from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")