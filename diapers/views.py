from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import status

from .models import Diapers
from .serializers import DiapersSerializer



class ListCreateDiapersView(generics.ListCreateAPIView):
    queryset = Diapers.objects.all()
    serializer_class = DiapersSerializer


class RetrieveUpdateDestroyDiapersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diapers.objects.all()
    serializer_class = DiapersSerializer


@api_view(['POST'])
def multi_delete_diapers(self, pk_list=None):
    delete_ids = pk_list.split(",")
    deleted_diapers = Diapers.objects.filter(pk__in=delete_ids).delete()
    data = {'diapers_deleted': deleted_diapers[0]}
    return Response(data, status=status.HTTP_200_OK)
