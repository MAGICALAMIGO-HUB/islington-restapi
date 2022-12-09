from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title