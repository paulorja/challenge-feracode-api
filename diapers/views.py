from rest_framework import generics
from .models import Diapers
from .serializers import DiapersSerializer


class ListDiapersView(generics.ListAPIView):
    queryset = Diapers.objects.all()
    serializer_class = DiapersSerializer


