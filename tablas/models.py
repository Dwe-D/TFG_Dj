from django.db import models

class numerosModel(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()
    

    #def __str__(self):
    #    return f"Números ({self.numero1}, {self.numero2})"