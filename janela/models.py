from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email único
    senha = models.CharField(max_length=128)  # Senha com tamanho adequado
    
    def __str__(self):
        return self.nome