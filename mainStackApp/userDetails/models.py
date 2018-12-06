from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import signals

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'username': self.user.username})

