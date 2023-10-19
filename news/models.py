from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    about = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

