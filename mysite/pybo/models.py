from datetime import datetime

from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    answer_one = models.CharField(max_length=200)
    answer_two = models.CharField(max_length=200)
    answer_three = models.CharField(max_length=200)
    answer_four = models.CharField(max_length=200)
    answer_right = models.IntegerField()

    def __str__(self):
        return self.question
