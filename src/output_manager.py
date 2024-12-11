import pandas as pd
import json
import xml.etree.ElementTree as ET

def save_to_json(filepath, data):
    """Save data to JSON file."""
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {filepath}")
    except Exception as e:
        print(f"Failed to save data to JSON: {e}")

def save_to_excel(filepath, data):
    """Save data to Excel file."""
    try:
        df = pd.DataFrame(data)
        df.to_excel(filepath, index=False)
        print(f"Data successfully saved to {filepath}")
    except Exception as e:
        print(f"Failed to save data to Excel: {e}")

def save_to_xml(filepath, data):
    """Save data to XML file."""
    try:
        root = ET.Element("Accounts")
        for account in data:
            account_elem = ET.SubElement(root, "Account")
            for key, value in account.items():
                ET.SubElement(account_elem, key).text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filepath)
        print(f"Data successfully saved to {filepath}")
    except Exception as e:
        print(f"Failed to save data to XML: {e}")

def save_data(filepath, data):
    """Save data dynamically based on file extension."""
    if filepath.endswith('.json'):
        save_to_json(filepath, data)
    elif filepath.endswith('.xlsx'):
        save_to_excel(filepath, data)
    elif filepath.endswith('.xml'):
        save_to_xml(filepath, data)
    else:
        raise ValueError("Unsupported file format. Please use .json, .xlsx, or .xml.")
