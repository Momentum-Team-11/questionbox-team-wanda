from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"
    def __str__(self):
        return self.username

class Question(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=True, related_name="questions")
    title=models.CharField(max_length=100, default=True, null=True)
    description=models.CharField(max_length=10000, default=True, null=True)
    created_at=models.DateField(auto_now_add=True)
    favorited=models.ManyToManyField(User, related_name="favorited_question", null=True, blank=True)
    def __str__(self):
        return self.title

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name="answers_list")
    response=models.CharField(max_length=10000, null=True, blank=True)
    answered=models.DateField(auto_now_add=True, null=True, blank=True)
    favorited=models.ManyToManyField(User, related_name="favorited_answer", null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name = "answer_user")
    def __str__(self):
        return str(self.response)
