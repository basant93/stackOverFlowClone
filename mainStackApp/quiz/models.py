from django.db import models

# Create your models here.
from django.utils import timezone

from django.contrib.auth.models import User
from django.urls import reverse


class QuestionTag(models.Model):
    name = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name

        super(QuestionTag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('question_tags', kwargs={'slug': self.slug})


class Question(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=255, unique = True)
    question_tag = models.ManyToManyField(QuestionTag, null=True, blank=True)
    question_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=timezone.now)
    view_count = models.BigIntegerField(default=1)
    rating = models.FloatField()
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title
        super(Question, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'slug': self.slug})


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.FloatField()

    def __str__(self):
        return u"id: %s question: %s text: %s " % (
            self.id, self.question, self.answer_text[:100])


class SavedQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    saved_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        unique_together = (('user', 'question'),)

    def __str__(self):
        return '%s %s' % (self.user, self.question.title)
