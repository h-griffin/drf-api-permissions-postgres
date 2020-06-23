from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Book
from .serializers import BooksSerializer
from .permissions import ISAuthorOrReadOnly

class BooksList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

class BooksDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

