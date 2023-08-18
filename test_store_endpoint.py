import unittest
import requests

class TestStoreEndpoint(unittest.TestCase):
    def test_get_inventory(self):
        response = requests.get("https://petstore.swagger.io/v2/store/inventory")
        self.assertEqual(response.status_code, 200)
        inventory_data = response.json()
        self.assertTrue(isinstance(inventory_data, dict))

if __name__ == "__main__":
    unittest.main()
