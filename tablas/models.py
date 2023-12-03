from django.db import models

class NumerosModel(models.Model):
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()

    def __str__(self):
        return f"Números ({self.numero1}, {self.numero2})"
