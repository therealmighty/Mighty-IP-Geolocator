import requests

def get_public_ip():
    """Fetch the user's public IP address."""
    response = requests.get("https://ipinfo.io/ip")
    return response.text.strip()

def lookup_ip(ip):
    """Use ip-api.com to get IP details."""
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    if data.get("status") != "success":
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

def save_to_file(info, filename="findings.txt"):
    """Save IP info to a text file."""
    with open(filename, "w") as f:
        f.write("==== IP Lookup Results ====\n")
        for key in ["IP", "Country", "Region", "ISP", "Organization", "Latitude", "Longitude"]:
            f.write(f"{key}: {info.get(key, 'N/A')}\n")

def main():
    ip = input("Enter IP address to lookup (leave blank for your own IP): ").strip()
    if not ip:
        print("No IP entered. Getting your public IP...")
        ip = get_public_ip()

    print(f"Looking up IP: {ip}")
    info = lookup_ip(ip)
    if info:
        save_to_file(info)
        print("Info saved to findings.txt")
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    main()
