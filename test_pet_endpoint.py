import unittest
import requests

class TestPetEndpoint(unittest.TestCase):
    def test_get_pet_by_id(self):
        response = requests.get("https://petstore.swagger.io/v2/pet/1")
        self.assertEqual(response.status_code, 200)
        pet_data = response.json()
        self.assertEqual(pet_data["id"], 1)

if __name__ == "__main__":
    unittest.main()
