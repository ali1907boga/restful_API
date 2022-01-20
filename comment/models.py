from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data']

class Like(models.Model):
    liker = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
