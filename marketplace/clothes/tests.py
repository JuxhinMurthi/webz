from rest_framework.test import APIClient
from rest_framework import status

from django.test import TestCase

from clothes.models import Garment
from authuser.models import User


class GarmentViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            address="123 Main St"
        )
        self.client.force_authenticate(user=self.user)
        self.garment_data = {
            "description": "Test Garment",
            "price": 19.99,
            "size": "MD",
            "type": "SH"
        }

    def test_create_garment(self):
        """ Test publishing a new garment """
        response = self.client.post("/api/clothes/publish/", self.garment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["description"], self.garment_data["description"])

    def test_update_garment(self):
        """ Test updating a garment by its publisher  """
        garment = Garment.objects.create(publisher=self.user, **self.garment_data)
        updated_data = {"description": "Updated Description"}
        response = self.client.put(f"/api/clothes/{garment.id}/update/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], "Updated Description")

    def test_delete_garment(self):
        """ Test deleting a garment by its publisher """
        garment = Garment.objects.create(publisher=self.user, **self.garment_data)
        response = self.client.delete(f"/api/clothes/{garment.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Garment.objects.filter(id=garment.id).exists())

    def test_cannot_update_others_garment(self):
        """ Test that a user cannot update someone else's garment """
        other_user = User.objects.create_user(
            username="otheruser",
            password="password123"
        )
        garment = Garment.objects.create(publisher=other_user, **self.garment_data)
        updated_data = {"description": "Unauthorized Update"}
        response = self.client.put(f"/api/clothes/{garment.id}/update/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_delete_others_garment(self):
        """Test that a user cannot delete someone else's garment"""
        other_user = User.objects.create_user(
            username="otheruser",
            password="password123"
        )
        garment = Garment.objects.create(publisher=other_user, **self.garment_data)
        response = self.client.delete(f"/api/clothes/{garment.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_garments_auth_not_required(self):
        """ Test retrieving a list of garments """
        Garment.objects.create(publisher=self.user, **self.garment_data)
        self.client.logout()
        response = self.client.get("/api/clothes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_get_single_garment_auth_not_required(self):
        """ Test retrieving a single garment by ID """
        garment = Garment.objects.create(publisher=self.user, **self.garment_data)
        self.client.logout()
        response = self.client.get(f"/api/clothes/{garment.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], self.garment_data["description"])

    def test_search_garments_auth_not_required(self):
        """ Test searching for garments by description """
        Garment.objects.create(publisher=self.user, **self.garment_data)
        self.client.logout()
        response = self.client.get("/api/clothes/", {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_auth_required_for_create(self):
        """ Test that authentication is required for publishing garments """
        self.client.force_authenticate(user=None)
        response = self.client.post("/api/clothes/publish/", self.garment_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_required_for_update(self):
        """ Test that authentication is required to update a garment """
        garment = Garment.objects.create(publisher=self.user, **self.garment_data)
        self.client.logout()
        updated_data = {"description": "Updated Description"}
        response = self.client.put(f"/api/clothes/{garment.id}/update/", updated_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_required_for_delete(self):
        """ Test that authentication is required to delete a garment """
        garment = Garment.objects.create(publisher=self.user, **self.garment_data)
        self.client.logout()
        response = self.client.delete(f"/api/clothes/{garment.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_garment_with_negative_price(self):
        """ Test that a garment cannot be created with a negative price """
        invalid_garment_data = {
            "description": "Invalid Garment",
            "price": -19.99,  # Invalid negative price
            "size": "MD",
            "type": "SH"
        }
        response = self.client.post("/api/clothes/publish/", invalid_garment_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("price", response.data)
        self.assertEqual(response.data["price"][0], "Price cannot be negative.")
