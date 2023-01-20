from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    def __str__(self):
        return f"Chat: {self.name} Author: {self.author.username}"

class Comment(models.Model):
    body = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True) # нужно сделать миграцию, поле со временем ещё не добавлено в БД

