from locations import locations
import random
import logging
import uuid
import time

def random_location():
    """Select a random location from the list."""
    try:
        location = random.choice(locations)
        logging.info(f"Selected random location: {location}")
        return location
    except Exception as e:
        logging.error(f"Failed to select random location: {e}")
        raise

def validate_account_data(data):
    """Validate account data to ensure all required fields are present."""
    required_keys = ["name", "birth_date", "gender"]
    try:
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required field: {key}")
        logging.info("Account data validation successful.")
        return True
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred during validation: {e}")
        raise
    
# Generate unique identifiers
def generate_device_id():
    """Generate a unique device ID."""
    return str(uuid.uuid4())

def generate_install_id():
    """Generate a unique install ID."""
    return str(uuid.uuid4())

def generate_session_id():
    """Generate a unique session ID."""
    return str(uuid.uuid4())

# Track elapsed time
class SessionTimer:
    def __init__(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        """Get the elapsed time since the session started."""
        return time.time() - self.start_time
