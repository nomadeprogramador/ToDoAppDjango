from django.db import models
# Create your models here.
class Tarefa (models.Model):
    conteudo=models.CharField(max_length=300)
    criado=models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return self.conteudo 
