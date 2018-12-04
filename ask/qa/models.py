from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_ad = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name="author")
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/question/%d" % self.pk


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.title
