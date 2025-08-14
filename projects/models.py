from django.db import models

class Project(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    f_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
