from django.db import models

# Create your models here.
class room(models.Model):
    code = models.CharField(max_length=6, default="", unique=True)
    host = models.CharField(max_length=20, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

