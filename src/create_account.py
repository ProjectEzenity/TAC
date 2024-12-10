import requests
import random
from config import TINDER_API_BASE, HEADERS
from utils import random_location, validate_account_data
from token_manager import load_token, refresh_token
from output_manager import save_to_json, save_to_excel, save_to_xml

def create_tinder_account(data, token):
  """Create a Tinder account using the API."""
  validate_account_data(data)
  location = random_location()
  payload = {
    "name": data["name"],
    "birth_date": data["birth_date"],  # Format: YYYY-MM-DD
    "gender": data["gender"],         # 0 for male, 1 for female
    "geo": location
  }
  headers = {**HEADERS, "Authorization": f"Bearer {token}"}
  response = requests.post(f"{TINDER_API_BASE}/v2/auth", json=payload, headers=headers)

  if response.status_code == 401:
    print("Token expired. Refreshing token...")
    token = refresh_token("../data/tinder_token.json", "https://api.tinder.com/v2/refresh", "your_client_id", "your_client_secret")
    headers["Authorization"] = f"Bearer {token}"
    response = requests.post(f"{TINDER_API_BASE}/v2/auth", json=payload, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    print(f"Failed to create account: {response.json()}")
    return None

if __name__ == "__main__":
  token = load_token("../data/tinder_token.json")["access_token"]

  # Example account data
  accounts = [
    {"name": "John Doe", "birth_date": "1990-01-01", "gender": 0},
    {"name": "Jane Doe", "birth_date": "1992-05-15", "gender": 1},
  ]

  results = []

  for account in accounts:
    result = create_tinder_account(account, token)
    if result:
      results.append(result)

  # Save results in various formats
  save_to_json("../data/output/accounts.json", results)
  save_to_excel("../data/output/accounts.xlsx", results)
  save_to_xml("../data/output/accounts.xml", results)
