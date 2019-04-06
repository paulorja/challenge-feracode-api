import json

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Diapers
from .serializers import DiapersSerializer



class GetAllDiapersTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_diaper(model="", size=""):
        if model != "" and size != "":
            Diapers.objects.create(model=model, size=size)

    def setUp(self):
        self.create_diaper("Huggies", "N")
        self.create_diaper("Huggies", "1")
        self.create_diaper("Huggies", "2")

        self.create_diaper("Honest", "N")
        self.create_diaper("Honest", "1")

    def test_get_all_diapers(self):
        response = self.client.get(
             reverse("diapers-list-create"),
        )

        expected = Diapers.objects.all()
        serialized = DiapersSerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateDiapersTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.valid_diaper = {
            'model': 'Pampers',
            'size': "4",
        }

    def test_create_diaper(self):
        response = self.client.post(
            reverse("diapers-list-create"),
            data=json.dumps(self.valid_diaper),
            content_type='application/json'
        )
        self.assertEqual(len(Diapers.objects.all()), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateDiapersTest(APITestCase):
    client = APIClient()

    def setUp(self):
        Diapers.objects.create(model="Pampers", size="4")
        self.valid_diaper = {
            'model': "Pampers",
            'size': "3",
        }

    def test_update_diaper(self):
        response = self.client.put(
            reverse("diapers-retrieve-update-destroy", kwargs={'pk': '1'}),
            data=json.dumps(self.valid_diaper),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteDiapersTest(APITestCase):
    client = APIClient()

    def setUp(self):
        Diapers.objects.create(model="Pampers", size="4")
        Diapers.objects.create(model="Pampers", size="5")

    def test_delete_diaper(self):
        response = self.client.delete(
            reverse("diapers-retrieve-update-destroy", kwargs={'pk': '1'}),
            content_type='application/json'
        )
        self.assertEqual(len(Diapers.objects.all()), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class MultiDeleteDiapersTest(APITestCase):
    client = APIClient()

    def setUp(self):
        Diapers.objects.create(model="Pampers", size="1")
        Diapers.objects.create(model="Pampers", size="2")
        Diapers.objects.create(model="Pampers", size="3")
        Diapers.objects.create(model="Pampers", size="4")
        Diapers.objects.create(model="Pampers", size="5")
        Diapers.objects.create(model="Pampers", size="6")

    def test_multi_delete_diapers(self):
        response = self.client.post(
            reverse("multi_delete_diapers", kwargs={'pk_list': '1, 3, 5'}),
            content_type='application/json'
        )
        self.assertEqual(response.data['diapers_deleted'], 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
