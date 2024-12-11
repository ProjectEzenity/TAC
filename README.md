# Tinder Account Creator

This project provides a script to create Tinder accounts using the Tinder API. It supports generating accounts with randomized geolocation data and saving account details in multiple formats such as JSON, Excel, and XML. The project is modular and designed for scalability, including token refreshing functionality and external location management.

## **Features**

- Create Tinder accounts using the API.
- Randomized geolocation selection for diverse user profiles.
- Supports saving account details in:
  - JSON
  - Excel
  - XML
- Modular design for easy maintenance and scalability.
- Automatic token refreshing for seamless API interactions.

## **Requirements**

- Python 3.8 or higher
- Required libraries (install via `pip`):
  - `requests`
  - `pandas`
  - `openpyxl`

## **Setup Instructions**

### Clone the Repository

```bash
git clone https://github.com/ProjectEzenity/TAC.git
cd TAC
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Project Structure

```text
TAC/
├── src/
│   ├── create_account.py        # Main script to create accounts
│   ├── utils.py                 # Utility functions
│   ├── token_manager.py         # Token handling logic
│   ├── output_manager.py        # Functions to save data in various formats
│   ├── config.py                # Configuration file for constants
│   ├── locations.py             # List of geolocations
├── data/
│   ├── input_data.xlsx          # Input data template
│   ├── snapchat_token.json      # Snapchat token file
│   ├── tinder_token.json        # Tinder token file
│   ├── output/
│   │   ├── accounts.json        # JSON output file
│   │   ├── accounts.xlsx        # Excel output file
│   │   ├── accounts.xml         # XML output file
├── tests/
│   ├── test_create_account.py   # Unit tests for the project
├── LICENSE                      # GNU General Public License v3.0
├── README.md                    # Project documentation
```

## **Configuration**

1. **Tinder Token**:
   - Obtain a valid Tinder API token and save it in `data/tinder_token.json`:

     ```json
     {
         "access_token": "your_tinder_access_token",
         "refresh_token": "your_refresh_token",
         "token_type": "Bearer",
         "expires_in": 3600
     }
     ```

2. **Snapchat Token**:
   - If required, save your Snapchat token in `data/snapchat_token.json`:

     ```json
     {
         "access_token": "your_snapchat_access_token",
         "refresh_token": "your_refresh_token",
         "token_type": "Bearer",
         "expires_in": 3600
     }
     ```

3. **Geolocations**:
   - Geolocations are managed in `src/locations.py` (Python) or `data/locations.json` (JSON).
   - To add more locations, edit the respective file.

4. **Input Data**:
   - Populate `data/input_data.xlsx` with account information (name, birth_date, gender).

5. **Dynamic Headers**:
   - The headers used for Tinder API requests are dynamically updated with session-specific data, including:
     - `persistent-device-id`: Generated at runtime.
     - `install-id`: Generated at runtime.
     - `app-session-id`: Generated at runtime.
     - `funnel-session-id`: Generated at runtime.
     - `app-session-time-elapsed`: Updated with the elapsed session time.
   - This ensures compliance with Tinder API requirements.

### Example Headers

```json
{
    "user-agent": "Tinder Android Version 12.6.0",
    "os-version": "25",
    "app-version": "4023",
    "platform": "android",
    "platform-variant": "Google-Play",
    "x-supported-image-formats": "webp",
    "accept-language": "en-US",
    "tinder-version": "12.6.0",
    "store-Variant": "Play-Store",
    "persistent-device-id": "123e4567-e89b-12d3-a456-426614174000",
    "content-type": "application/x-protobuf",
    "host": "api.gotinder.com",
    "connection": "close",
    "accept-encoding": "gzip,deflate, br",
    "install-id": "123e4567-e89b-12d3-a456-426614174001",
    "app-session-id": "123e4567-e89b-12d3-a456-426614174002",
    "funnel-session-id": "123e4567-e89b-12d3-a456-426614174003",
    "app-session-time-elapsed": "0.123"
}
```

### Example Header Initialization

```python
from config import update_headers
from utils import generate_device_id, generate_install_id, generate_session_id, SessionTimer

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
```

## **How It Works**

1. **Header Initialization**:
   - At the start of the script, unique session identifiers are generated and headers are dynamically updated.
2. **Input Data Loading**:
   - User data is loaded from `data/input_data.xlsx` or other supported formats (JSON, XML).
3. **Account Creation**:
   - For each account, the script validates the input, assigns a random geolocation, and sends the request to Tinder API.
4. **Token Management**:
   - If the token expires, it is refreshed automatically using the refresh token.
5. **Output Generation**:
   - Results are saved in JSON, Excel, and XML formats for easy reference.

## **Usage**

### Run the Script

To create accounts, run the main script:

```bash
python src/create_account.py
```

### Output Files

- JSON: `data/output/accounts.json`
- Excel: `data/output/accounts.xlsx`
- XML: `data/output/accounts.xml`

### Randomized Locations

Locations are randomized for each account using the `random_location()` function. The list of locations can be extended in `locations.py` or `locations.json`.

## **Key Functions**

### `src/create_account.py`

- Main script for creating accounts.
- Handles:
  - Input validation.
  - Token refreshing.
  - Saving results in multiple formats.

### `src/token_manager.py`

- Manages API token lifecycle, including:
  - Loading tokens.
  - Saving tokens.
  - Refreshing tokens if expired.

### `src/output_manager.py`

- Saves account details in:
  - JSON
  - Excel
  - XML

### `src/locations.py`

- Contains a list of geolocations for randomization.

## **Examples**

### Example Input Data (`data/input_data.xlsx`)

| Name       | Birth Date  | Gender |
|------------|-------------|--------|
| John Doe   | 1990-01-01  | 0      |
| Jane Smith | 1992-05-15  | 1      |

### Example JSON Output

```json
[
    {
        "name": "John Doe",
        "birth_date": "1990-01-01",
        "gender": 0,
        "location": {"lat": 40.7128, "lon": -74.0060},
        "status": "success"
    },
    {
        "name": "Jane Smith",
        "birth_date": "1992-05-15",
        "gender": 1,
        "location": {"lat": 51.5074, "lon": -0.1278},
        "status": "success"
    }
]
```

### Example Command

Run the script and view the outputs:

```bash
python src/create_account.py
```

## **Extending the Project**

- **Adding Locations**:
  - Edit `src/locations.py` or `data/locations.json` to include more geolocations.
- **Additional Formats**:
  - Extend `output_manager.py` to support other formats like CSV or database integration.
- **Input Sources**:
  - Modify `create_account.py` to load input data from APIs or other sources.

## **Troubleshooting**

- **Token Expired**:
  - Ensure the `refresh_token` is valid and the refresh URL in `token_manager.py` is correct.
  - If you encounter a `401 Unauthorized` error, ensure your `refresh_token` is valid.
  - Check the `logs/app.log` file for detailed error messages.
- **HTTP Errors**:
  - Ensure that your internet connection is stable.
  - Refer to the error logs to identify specific issues with the API response.
- **Missing Dependencies**:
  - Install missing libraries with `pip install -r requirements.txt`.


## **License**

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## **Contributions**

Contributions are welcome! Feel free to open an issue or submit a pull request.
