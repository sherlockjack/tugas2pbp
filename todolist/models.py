from pydoc import describe
from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class todolistItem(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    title=models.CharField(max_length=255)
    description=models.TextField()
    is_finished = models.BooleanField(default=False )
