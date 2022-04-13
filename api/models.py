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
    title=models.CharField(max_length=100, default=True, blank=False)
    description=models.CharField(max_length=10000, default=True, blank=False)
    created_at=models.DateField(auto_now_add=True)
    favorited=models.ManyToManyField(User, related_name="favorited_question", blank=True)
    def __str__(self):
        return self.title

class Answer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers_list")
    response=models.CharField(max_length=10000, blank=False, default=True)  
    answered=models.DateField(auto_now_add=True)
    favorited=models.ManyToManyField(User, related_name="favorited_answer", blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name = "answer_user")
    correct=models.BooleanField(default=False)
    def __str__(self):
        return str(self.response)



