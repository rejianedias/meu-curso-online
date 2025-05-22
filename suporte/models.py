from django.db import models

class FAQ(models.Model):
    pergunta = models.CharField(max_length=200)
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta


# Create your models here.
