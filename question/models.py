from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Question(models.Model):
    question_text = models.TextField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User,
                                 null=True, blank=True, on_delete=models.CASCADE, default=None)
    category = models.CharField(max_length=40, blank=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User,
                                 null=True, blank=True, on_delete=models.CASCADE, default=None)
    votes = models.IntegerField(default=0)
