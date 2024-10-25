from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Dog
from .serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [AllowAny]
