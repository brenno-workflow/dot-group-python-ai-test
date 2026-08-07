from django.shortcuts import render
from rest_framework import generics, status
from .models import Book
from .services.serializers import BookSerializer
from rest_framework.response import Response

# Create your views here.

# Adicionar livro
class PostBookView(generics.CreateAPIView):
    """
    Endpoint responsável exclusivamente pelo cadastro de livros.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Pesquisar livro
class GetBookView(generics.ListAPIView):
    """
    Endpoint responsável pela consulta de livros.
    O retorno é sempre uma lista, mesmo quando apenas um livro for encontrado.
    """

    serializer_class = BookSerializer

    # Buscar no banco
    def get_queryset(self):
        queryset = Book.objects.filter(is_active=True)

        # Dicionários de filtros
        filter_mapping = {
            "id": "id",
            "title": "title__icontains",
            "author": "author__icontains",
            "publication_date": "publication_date",
            "summary": "summary__icontains",
            "created_at": "created_at__date",
            "updated_at": "updated_at__date",
        }

        # Filtrar
        for param_name, lookup in filter_mapping.items():
            value = self.request.query_params.get(param_name)
            if value: queryset = queryset.filter(**{lookup: value})

        # Return
        return queryset

    # Listar para nao quebrar
    def list(self, request, *args, **kwargs):
        """
        Executa a busca e retorna uma mensagem amigável caso ocorra erro.
        """

        # TryCath
        try:
            return super().list(request, *args, **kwargs)

        # Except
        except Exception as e:
            return Response({"error": "Erro ao pesquisar livros.", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)