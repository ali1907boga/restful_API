from django.db import models
from datetime import datetime



class Journalist(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.ForeignKey(Journalist,on_delete=models.CASCADE,null=True,blank=True,related_name='book')
    store_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='store_image/',null=True)
    fav = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name.author} || {self.store_name}'


