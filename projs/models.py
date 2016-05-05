from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Empregado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + " - " + self.titulo


class Projecto(models.Model):
    autor = models.ForeignKey(Empregado,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    votos = models.IntegerField(default=0)
    texto = models.TextField(max_length=2000,default="")
    data = models.DateTimeField(default=timezone.now)

    def publicaProj(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    proj = models.ForeignKey(Projecto, on_delete=models.CASCADE)
    autor = models.CharField(max_length=200)
    texto = models.TextField(max_length=2000,default="")
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.autor
