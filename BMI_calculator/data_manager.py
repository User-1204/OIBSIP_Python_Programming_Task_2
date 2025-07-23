# data_manager.py
# Handles loading/saving data and exporting to CSV

import json, csv, os
from constants import DATA_FILE

def load_data():
    if os.path.exists(DATA_FILE):  # Check if file exists
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    # Return empty dict if file missing    
    return {} 

def save_data(data):
    with open(DATA_FILE, "w") as f:
        # Write data with indentation
        json.dump(data, f, indent=4) 

def export_to_csv(name, entries):
    # Filename based on user name
    filename = f"bmi_export_{name}.csv"  
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date/Time", "Weight (kg)", "Height (m)", "BMI", "Category"])
        for e in entries: 
            writer.writerow([e["time"], e["weight"], e["height"], e["bmi"], e["category"]])
    return filename
