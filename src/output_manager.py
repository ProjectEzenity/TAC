import pandas as pd
import json
import xml.etree.ElementTree as ET

def save_to_json(filepath, data):
  """Save data to JSON file."""
  with open(filepath, 'w') as file:
    json.dump(data, file, indent=4)

def save_to_excel(filepath, data):
  """Save data to Excel file."""
  df = pd.DataFrame(data)
  df.to_excel(filepath, index=False)

def save_to_xml(filepath, data):
  """Save data to XML file."""
  root = ET.Element("Accounts")
  for account in data:
    account_elem = ET.SubElement(root, "Account")
    for key, value in account.items():
      ET.SubElement(account_elem, key).text = str(value)
  tree = ET.ElementTree(root)
  tree.write(filepath)