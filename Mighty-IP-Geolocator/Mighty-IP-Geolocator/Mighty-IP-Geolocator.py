import requests
import os

def get_public_ip():
    """Fetch the user's public IP address."""
    try:
        response = requests.get("https://ipinfo.io/ip")
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print("Error getting public IP:", e)
        return None

def lookup_ip(ip):
    """Use ip-api.com to get IP details."""
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()
        if data.get("status") != "success":
            print("Lookup failed:", data)
            return None

        return {
            "IP": data.get("query", "N/A"),
            "Country": data.get("country", "N/A"),
            "Region": data.get("regionName", "N/A"),
            "ISP": data.get("isp", "N/A"),
            "Organization": data.get("org", "N/A"),
            "Latitude": data.get("lat", "N/A"),
            "Longitude": data.get("lon", "N/A")
        }
    except Exception as e:
        print("Error during IP lookup:", e)
        return None

def save_to_file(info, filename="output/IP-Log.txt"):
    """Save IP info to a text file in the 'output' folder."""
    try:
        os.makedirs("output", exist_ok=True)
        with open(filename, "w") as f:
            f.write("==== IP Lookup Results ====\n")
            for key in info:
                f.write(f"{key}: {info[key]}\n")
        print(f"Info saved to {filename}")
    except Exception as e:
        print("Error saving to file:", e)

def main():
    ip = input("Enter IP address to lookup (leave blank for your own IP): ").strip()
    if not ip:
        print("No IP entered. Getting your public IP...")
        ip = get_public_ip()
        if not ip:
            print("Could not get public IP. Exiting.")
            input("Press Enter to exit...")
            return

    print(f"Looking up IP: {ip}")
    info = lookup_ip(ip)
    if info:
        save_to_file(info)
    else:
        print("Failed to retrieve IP data.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
