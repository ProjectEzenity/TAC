import requests
import json
import logging

def load_token(filepath):
    """Load token from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            token = json.load(file)
        logging.info(f"Token successfully loaded from {filepath}")
        return token
    except Exception as e:
        logging.error(f"Failed to load token from {filepath}: {e}")
        raise

def save_token(filepath, token_data):
    """Save token to a JSON file."""
    try:
        with open(filepath, 'w') as file:
            json.dump(token_data, file, indent=4)
        logging.info(f"Token successfully saved to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save token to {filepath}: {e}")
        raise

def refresh_token(filepath, refresh_url, client_id, client_secret):
    """Refresh the API token using the refresh token."""
    try:
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
            logging.info("Token successfully refreshed.")
            return new_token_data["access_token"]
        else:
            logging.error(f"Failed to refresh token: {response.json()}")
            response.raise_for_status()
    except Exception as e:
        logging.error(f"An error occurred during token refresh: {e}")
        raise
