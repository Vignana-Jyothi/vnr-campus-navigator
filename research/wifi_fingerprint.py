import os
import time
import pandas as pd
from wifi import Cell, Scheme

def scan_wifi():
    # Scan for available Wi-Fi networks and return their signal strengths
    cells = Cell.all('wlan0')
    wifi_data = []
    for cell in cells:
        wifi_data.append({
            'ssid': cell.ssid,
            'signal': cell.signal
        })
    return wifi_data

def create_fingerprint_database():
    # Create a database of Wi-Fi fingerprints at known locations
    fingerprint_db = pd.DataFrame(columns=['location', 'ssid', 'signal'])
    locations = ['location1', 'location2', 'location3']  # Example locations
    for location in locations:
        print(f"Scanning Wi-Fi at {location}...")
        wifi_data = scan_wifi()
        for data in wifi_data:
            fingerprint_db = fingerprint_db.append({
                'location': location,
                'ssid': data['ssid'],
                'signal': data['signal']
            }, ignore_index=True)
        time.sleep(5)  # Wait between scans
    fingerprint_db.to_csv('wifi_fingerprint_db.csv', index=False)
    print("Fingerprint database created.")

def locate():
    # Estimate current location based on Wi-Fi fingerprinting
    fingerprint_db = pd.read_csv('wifi_fingerprint_db.csv')
    current_scan = scan_wifi()
    location_scores = {}
    for index, row in fingerprint_db.iterrows():
        location = row['location']
        ssid = row['ssid']
        signal = row['signal']
        for data in current_scan:
            if data['ssid'] == ssid:
                if location not in location_scores:
                    location_scores[location] = 0
                location_scores[location] += abs(signal - data['signal'])
    estimated_location = min(location_scores, key=location_scores.get)
    print(f"Estimated Location: {estimated_location}")

if __name__ == "__main__":
    create_fingerprint_database()
    locate()
