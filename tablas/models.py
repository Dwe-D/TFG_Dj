from django.db import models

class sensores(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()
    numero3 = models.FloatField()
    booleano = models.BooleanField(default=True)

    #def __str__(self):
    #    return f"Números ({self.numero1}, {self.numero2})"
