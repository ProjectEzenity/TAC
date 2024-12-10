import pandas as pd
import json
import xml.etree.ElementTree as ET

def load_excel(filepath):
  """Load data from Excel."""
  return pd.read_excel(filepath)

def load_json(filepath):
  """Load data from JSON."""
  with open(filepath, 'r') as file:
    return json.load(file)
  
def load_xml(filepath):
  """Load data from XML."""
  tree = ET.parse(filepath)
  return tree.getroot()