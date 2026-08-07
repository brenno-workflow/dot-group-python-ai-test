from django.db import models

# Create your models here.

# Tabela de livros
class Book(models.Model):
    """
    Representa um livro disponível na biblioteca virtual.
    """

    # Campos solicitados
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()
    summary = models.TextField()

    # Campos de controle
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Retorna uma representação legível do livro.
        """

        return f"{self.title} - {self.author}"