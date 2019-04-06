from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Diapers
from .serializers import DiapersSerializer


class ListCreateDiapersView(generics.ListCreateAPIView):
    queryset = Diapers.objects.all()
    serializer_class = DiapersSerializer

class RetrieveUpdateDestroyDiapersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diapers.objects.all()
    serializer_class = DiapersSerializer
