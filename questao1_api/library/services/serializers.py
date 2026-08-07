from rest_framework import serializers
from ..models import Book

# Classe de chamada
class BookSerializer(serializers.ModelSerializer):
    """
    Classe responsável por converter instâncias do DB para JSON e validar os dados recebidos nas requisições da API.
    """

    class Meta:
        model = Book
        fields = ["id", "title", "author", "publication_date", "summary", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]