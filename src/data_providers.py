import pandas as pd
import json
import xml.etree.ElementTree as ET

def load_excel(filepath):
    """Load data from Excel."""
    df = pd.read_excel(filepath)
    return df.to_dict(orient="records")

def load_json(filepath):
    """Load data from JSON."""
    with open(filepath, 'r') as file:
        return json.load(file)

def load_xml(filepath):
    """Load data from XML."""
    tree = ET.parse(filepath)
    root = tree.getroot()
    data = []
    for child in root:
        record = {elem.tag: elem.text for elem in child}
        data.append(record)
    return data

def load_accounts(filepath):
    """Dynamically load accounts based on file extension."""
    if filepath.endswith('.xlsx'):
        return load_excel(filepath)
    elif filepath.endswith('.json'):
        return load_json(filepath)
    elif filepath.endswith('.xml'):
        return load_xml(filepath)
    else:
        raise ValueError("Unsupported file format. Please use .xlsx, .json, or .xml.")
