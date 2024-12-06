import urllib.request
import json
import os

# Replace with your NOAA API Token
API_TOKEN = "YYXVOvUbiurcrpTWCErQzxGBAFaefpyh"

# Base URL for the locations endpoint
BASE_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations"

# Headers for the request
HEADERS = {
    "Token": API_TOKEN
}

# Number of results per request
LIMIT = 1000


OUTPUT_DIR = "locations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for i in range(39): 
    offset = i * LIMIT + 1
    print(f"Fetching data for offset {offset}...")
    
    # Prepare the URL
    url = f"{BASE_URL}?limit={LIMIT}&offset={offset}"
    
    try:
        # Fetch data
        request = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(request) as response:
            if response.status != 200:
                raise Exception(f"HTTP Error: {response.status}")
            data = json.loads(response.read().decode())
        
        # Write the data to a file
        filename = f"{OUTPUT_DIR}/locations_{i}.json"
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Saved data to {filename}")
    except Exception as e:
        print(f"Failed to fetch data for offset {offset}: {e}")
        continue

print("All files created successfully.")