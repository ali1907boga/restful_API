from django.db import models
from django.contrib.auth.models import User

class Comment1(models.Model):
    text1 = models.TextField()
    author1 = models.ForeignKey(User,on_delete=models.CASCADE)
    data1 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author1.username

class Like1(models.Model):
    liker1 = models.ForeignKey(User,on_delete=models.CASCADE)
    comment1 = models.ForeignKey(Comment1,on_delete=models.CASCADE)

    def __str__(self):
        return self.liker1.username