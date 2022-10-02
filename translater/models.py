from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)




