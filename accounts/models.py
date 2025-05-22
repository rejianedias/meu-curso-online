from django.contrib.auth.models import AbstractUser
from django.db import models

#Importações**: importa o `AbstractUser`, que é uma versão estendível do sistema de autenticação do Django, e os utilitários de modelos do Django.

class CustomUser(AbstractUser):
    
    #- **Campo personalizado**: adiciona um novo campo chamado `nome_completo` ao modelo de usuário.
    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    #- **Campo principal de login**: define que o campo `username` continuará sendo usado como identificador principal para login (padrão do Django).
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nome_completo']

    #- **Representação do objeto**: define como o objeto será representado como string — neste caso, pelo nome de usuário.
    def __str__(self):
        return self.username

# Create your models here.
