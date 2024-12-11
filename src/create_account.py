import requests
import random
import logging
from tenacity import retry, stop_after_attempt, wait_fixed
from config import TINDER_API_BASE, HEADERS, update_headers
from utils import random_location, validate_account_data, generate_device_id, generate_install_id, generate_session_id, SessionTimer
from token_manager import load_token, refresh_token
from output_manager import save_to_json, save_to_excel, save_to_xml
from data_providers import load_accounts

# Configure logging
logging.basicConfig(filename="../logs/app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def make_api_request(url, payload, headers):
    """Make a POST request to the Tinder API with retry logic."""
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response

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
    try:
        response = make_api_request(f"{TINDER_API_BASE}/v2/auth", payload, headers)
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f"Connection error occurred: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f"Timeout error occurred: {timeout_err}")
        return None
    except Exception as err:
        logging.error(f"An unexpected error occurred: {err}")
        return None

    if response.status_code == 401:
        logging.warning("Token expired. Refreshing token...")
        token = refresh_token("../data/tinder_token.json", "https://api.tinder.com/v2/refresh", "your_client_id", "your_client_secret")
        headers["Authorization"] = f"Bearer {token}"
        response = requests.post(f"{TINDER_API_BASE}/v2/auth", json=payload, headers=headers)

    if response.status_code == 200:
        logging.info("Account created successfully.")
        return response.json()
    else:
        logging.error(f"Failed to create account: {response.json()}")
        return None

def initialize_headers():
    """Generate IDs, start timer, and update headers."""
    device_id = generate_device_id()
    install_id = generate_install_id()
    app_session_id = generate_session_id()
    funnel_id = generate_session_id()

    session_timer = SessionTimer()

    update_headers(
        device_id=device_id,
        install_id=install_id,
        app_session_id=app_session_id,
        funnel_id=funnel_id,
        elapsed_time=session_timer.get_elapsed_time()
    )

    return session_timer

if __name__ == "__main__":
    logging.info("Starting account creation process.")

    session_timer = initialize_headers()

    # Load account data from Excel
    token = load_token("../data/tinder_token.json")["access_token"]
    accounts = load_accounts("../data/input_data.xlsx")
    results = []

    for account in accounts:
        result = create_tinder_account(account, token)
        if result:
            results.append(result)

    # Save results in various formats
    save_to_json("../data/output/accounts.json", results)
    save_to_excel("../data/output/accounts.xlsx", results)
    save_to_xml("../data/output/accounts.xml", results)

    logging.info("Account creation process completed.")
