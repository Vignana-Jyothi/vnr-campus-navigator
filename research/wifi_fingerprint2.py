import subprocess
import pandas as pd
import time

## Prereqs: sudo apt-get install iw
## change the interface value based on ifconfig output

def scan_wifi(interface='wlp0s20f3'):
    try:
        result = subprocess.check_output(['sudo', 'iw', interface, 'scan'])
        result = result.decode('utf-8')
        return parse_scan_result(result)
    except subprocess.CalledProcessError as e:
        print(f"Error scanning Wi-Fi: {e}")
        return []

def parse_scan_result(scan_result):
    wifi_data = []
    cells = scan_result.split('BSS ')
    for cell in cells[1:]:
        ssid = None
        signal = None
        for line in cell.split('\n'):
            if 'SSID:' in line:
                ssid = line.split('SSID: ')[1].strip()
            if 'signal:' in line:
                signal = float(line.split('signal: ')[1].split(' ')[0])
        if ssid and signal:
            wifi_data.append({
                'ssid': ssid,
                'signal': signal
            })
    return wifi_data

def create_fingerprint_database():
    fingerprint_db = pd.DataFrame(columns=['location', 'ssid', 'signal'])
    locations = ['location1', 'location2', 'location3']
    for location in locations:
        print(f"Scanning Wi-Fi at {location}...")
        wifi_data = scan_wifi()
        for data in wifi_data:
            new_row = pd.DataFrame([{
                'location': location,
                'ssid': data['ssid'],
                'signal': data['signal']
            }])
            fingerprint_db = pd.concat([fingerprint_db, new_row], ignore_index=True)
        time.sleep(5)  # Wait between scans
    fingerprint_db.to_csv('wifi_fingerprint_db.csv', index=False)
    print("Fingerprint database created.")

def locate():
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
    if not location_scores:
        print("No matching Wi-Fi networks found.")
        return
    estimated_location = min(location_scores, key=location_scores.get)
    print(f"Estimated Location: {estimated_location}")

if __name__ == "__main__":
    create_fingerprint_database()
    locate()
