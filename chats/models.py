from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="me")
    frnd = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="my_frd")
    chats = models.JSONField(default=dict)
