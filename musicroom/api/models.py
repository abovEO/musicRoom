from django.db import models
import string
import random

def generate_code():
    while True:
        generated_code = "".join(random.choices(string.ascii_letters, k=6))
        if room.objects.filter(code=generated_code).count() == 0 :
            break
    return generated_code

# Create your models here.
class room(models.Model):
    code = models.CharField(max_length=6, default="", unique=True)
    host = models.CharField(max_length=20, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

