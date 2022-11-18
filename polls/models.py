from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    date = models.DateTimeField("date published")
    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.date <= now
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

