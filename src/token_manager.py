import requests
import json

def load_token(filepath):
  """Load token from a JSON file."""
  with open(filepath, 'r') as file:
    return json.load(file)

def save_token(filepath, token_data):
  """Save token to a JSON file."""
  with open(filepath, 'w') as file:
    json.dump(token_data, file, indent=4)

def refresh_token(filepath, refresh_url, client_id, client_secret):
  """Refresh the API token using the refresh token."""
  token_data = load_token(filepath)
  response = requests.post(refresh_url, data={
    "grant_type": "refresh_token",
    "refresh_token": token_data["refresh_token"],
    "client_id": client_id,
    "client_secret": client_secret
  })

  if response.status_code == 200:
    new_token_data = response.json()
    save_token(filepath, new_token_data)
    return new_token_data["access_token"]
  else:
    raise Exception(f"Failed to refresh token: {response.json()}")
