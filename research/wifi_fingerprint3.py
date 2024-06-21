import subprocess
import pandas as pd
import time

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
        bssid = None
        ssid = None
        signal = None
        lines = cell.split('\n')
        if lines:
            # Check first line for BSSID
            first_line_parts = lines[0].strip().split()
            if len(first_line_parts) > 1:
                bssid = first_line_parts[0].strip()
        for line in lines:
            if 'SSID:' in line:
                ssid = line.split('SSID: ')[1].strip()
            elif 'signal:' in line:
                signal = float(line.split('signal: ')[1].split(' ')[0])
        
        # Debugging Output
        if bssid and ssid is not None and signal is not None:
            wifi_data.append({
                'bssid': bssid,
                'ssid': ssid,
                'signal': signal
            })
        else:
            print(f"Skipping incomplete data: BSSID={bssid}, SSID={ssid}, Signal={signal}")
    return wifi_data

def print_scan_data(wifi_data):
    if not wifi_data:
        print("No Wi-Fi networks found.")
        return

    print(f"{'BSSID':<20} {'SSID':<30} {'Signal Strength (dBm)':<20}")
    print("="*70)
    for data in wifi_data:
        print(f"{data['bssid']:<20} {data['ssid']:<30} {data['signal']:<20}")

def create_fingerprint_database():
    fingerprint_db = pd.DataFrame(columns=['location', 'bssid', 'ssid', 'signal'])
    locations = ['location1', 'location2', 'location3']
    for location in locations:
        print(f"\nScanning Wi-Fi at {location}...")
        wifi_data = scan_wifi()
        print_scan_data(wifi_data)
        for data in wifi_data:
            new_row = pd.DataFrame([{
                'location': location,
                'bssid': data['bssid'],
                'ssid': data['ssid'],
                'signal': data['signal']
            }])
            fingerprint_db = pd.concat([fingerprint_db, new_row], ignore_index=True)
        time.sleep(5)  # Wait between scans
    fingerprint_db.to_csv('wifi_fingerprint_db.csv', index=False)
    print("\nFingerprint database created.")

def locate():
    fingerprint_db = pd.read_csv('wifi_fingerprint_db.csv')
    current_scan = scan_wifi()
    print("\nCurrent Wi-Fi Scan:")
    print_scan_data(current_scan)
    location_scores = {}
    for index, row in fingerprint_db.iterrows():
        location = row['location']
        bssid = row['bssid']
        signal = row['signal']
        for data in current_scan:
            if data['bssid'] == bssid:
                if location not in location_scores:
                    location_scores[location] = 0
                location_scores[location] += abs(signal - data['signal'])
    if not location_scores:
        print("No matching Wi-Fi networks found.")
        return
    estimated_location = min(location_scores, key=location_scores.get)
    print(f"\nEstimated Location: {estimated_location}")

if __name__ == "__main__":
    create_fingerprint_database()
    locate()
