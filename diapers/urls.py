from django.urls import path
from .views import ListDiapersView


urlpatterns = [
    path('diapers/', ListDiapersView.as_view(), name="diapers-all")
]

