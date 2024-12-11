import unittest
from src.create_account import create_tinder_account
from src.token_manager import load_token
from src.utils import validate_account_data, random_location
from unittest.mock import patch, MagicMock

class TestCreateAccount(unittest.TestCase):
    @patch('src.create_account.requests.post')
    def test_create_tinder_account_success(self, mock_post):
        """Test successful account creation."""
        # Mock API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "id": "12345"}
        mock_post.return_value = mock_response

        # Sample account data
        account_data = {
            "name": "John Doe",
            "birth_date": "1990-01-01",
            "gender": 0
        }
        token = "test_token"

        result = create_tinder_account(account_data, token)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["id"], "12345")

    def test_validate_account_data_missing_field(self):
        """Test validation with missing fields."""
        account_data = {
            "name": "John Doe",
            "birth_date": "1990-01-01"
        }
        with self.assertRaises(ValueError):
            validate_account_data(account_data)

    def test_random_location(self):
        """Test random location selection."""
        location = random_location()
        self.assertIn("lat", location)
        self.assertIn("lon", location)

if __name__ == "__main__":
    unittest.main()
