from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import signals
from quiz.models import Question, Answer
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Answer)
def add_answer_reputation(sender, instance, **kwargs):
    """
    Increase reputation for every answer given.
    """
    user_id = instance.author_id
    user_obj = get_object_or_404(User, id=user_id)
    user_obj.reputation +=1
    user_obj.save()


@receiver(post_save, sender=Question)
def add_question_reputation(sender, instance, **kwargs):
    """
    Increase reputation for every question asked.
    """
    user_id = instance.author_id
    user_obj = get_object_or_404(User, id=user_id)
    user_obj.reputation +=1
    user_obj.save()
    