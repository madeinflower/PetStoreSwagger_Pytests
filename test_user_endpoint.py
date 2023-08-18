import unittest
import requests

class TestUserEndpoint(unittest.TestCase):
    def test_create_user(self):
        user_data = {
            "id": 1,
            "username": "testuser",
            "firstName": "John",
            "lastName": "Doe",
            "email": "testuser@example.com",
            "password": "secretpassword",
            "phone": "1234567890",
            "userStatus": 1
        }

        response = requests.post("https://petstore.swagger.io/v2/user", json=user_data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_username(self):
        username = "testuser"
        response = requests.get(f"https://petstore.swagger.io/v2/user/{username}")
        self.assertEqual(response.status_code, 200)
        user_data = response.json()
        self.assertEqual(user_data["username"], username)

if __name__ == "__main__":
    unittest.main()
