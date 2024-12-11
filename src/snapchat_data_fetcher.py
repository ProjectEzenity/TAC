import requests
import json
import logging

def load_snapchat_auth(filepath):
    """Load Snapchat authentication details from a JSON file."""
    try:
        with open(filepath, 'r') as file:
            auth_data = json.load(file)
        logging.info(f"Snapchat auth details successfully loaded from {filepath}")
        return auth_data
    except Exception as e:
        logging.error(f"Failed to load Snapchat auth details: {e}")
        raise

def fetch_snapchat_user_data(auth_data, output_filepath):
    """Fetch user name and images from Snapchat API."""
    base_url = "https://kit.snapchat.com/v1/me"  # Adjust API endpoint as needed
    headers = {
        "Authorization": f"Bearer {auth_data['access_token']}"
    }

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        user_data = response.json()

        # Extract relevant data
        name = user_data.get("name", "Unknown")
        images = user_data.get("images", [])

        # Save to output file
        save_to_json(output_filepath, {"name": name, "images": images})
        logging.info(f"Snapchat user data successfully saved to {output_filepath}")
        return {"name": name, "images": images}

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred: {timeout_err}")
    except Exception as err:
        logging.error(f"An unexpected error occurred: {err}")


def save_to_json(filepath, data):
    """Save data to JSON file."""
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data successfully saved to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save data to JSON: {e}")
        raise

if __name__ == "__main__":
    logging.basicConfig(filename="../logs/snapchat_fetch.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Load Snapchat authentication details
    auth_data = load_snapchat_auth("../data/snapchat_token.json")

    # Fetch and save Snapchat user data
    output_filepath = "../data/output/accounts.json"
    user_data = fetch_snapchat_user_data(auth_data, output_filepath)

    # Print fetched data
    print(user_data)
