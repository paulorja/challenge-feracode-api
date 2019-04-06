from django.urls import path

from diapers import views


urlpatterns = [
    path('diapers/', views.ListCreateDiapersView.as_view(), name="diapers-list-create"),
    path('diapers/<pk>/', views.RetrieveUpdateDestroyDiapersView.as_view(), name="diapers-retrieve-update-destroy"),
    path('multi_delete_diapers/<pk_list>/', views.multi_delete_diapers, name="multi_delete_diapers")
]

