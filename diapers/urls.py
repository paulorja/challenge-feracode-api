from django.urls import path
from .views import ListCreateDiapersView


urlpatterns = [
    path('diapers/', ListCreateDiapersView.as_view(), name="diapers-list-create"),
]

