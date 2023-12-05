from django.db import models

# Create your models here.

class sensores(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()