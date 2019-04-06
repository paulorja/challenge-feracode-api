from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Diapers
from .serializers import DiapersSerializer



class BaseViewTest(APITestCase):
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


class GetAllDiapersTest(BaseViewTest):

    def test_get_all_diapers(self):
        response = self.client.get(
            reverse("diapers-all", kwargs={"version": "v1"})
        )

        expected = Diapers.objects.all()
        serialized = DiapersSerializer(expected, many=True)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

