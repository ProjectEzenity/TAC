from locations import locations
import random

def random_location():
  """Select a random location fromthe list."""
  return random.choice(locations)

def validate_account_data(data):
  """Validate account data to ensure all required fields are present."""
  required_keys = ["name", "birth_date", "gender"]
  for key in required_keys:
    if key not in data:
      raise ValueError(f"Missing required field: {key}")
  return True
