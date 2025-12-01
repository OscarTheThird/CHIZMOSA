import numpy as np
import os
import json

# Path to your label_map.npy
BASE_PATH = '..'
# --- MODIFIED: Look for label_map.npy directly in the root folder ---
LABEL_PATH = os.path.join(BASE_PATH, 'label_map.npy')

if not os.path.exists(LABEL_PATH):
    print(f"Error: File not found at {LABEL_PATH}")
    # Update the error message to reflect the new location
    print("Please ensure 'label_map.npy' is in the root project folder.")
else:
    # Load the dictionary
    label_map = np.load(LABEL_PATH, allow_pickle=True).item()
    
    print("-" * 30)
    print("CONTENTS OF label_map.npy")
    print("-" * 30)
    print(label_map)
    print("-" * 30)
    
    # Print as a clean list for your JSON file
    print("\nCopy this list for your 'labels.json':")
    
    # Sort by ID to ensure correct order
    sorted_labels = sorted(label_map.items(), key=lambda item: item[1])
    clean_list = [label for label, _ in sorted_labels]
    
    print(json.dumps(clean_list, indent=2))