from django.urls import path

from diapers import views


urlpatterns = [
    path('diapers/', views.ListCreateDiapersView.as_view(), name="diapers-list-create"),
    path('diapers/<pk>/', views.RetrieveUpdateDestroyDiapersView.as_view(), name="diapers-retrieve-update-destroy"),
]

