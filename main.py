import requests, time

API_KEY = 'yourapikeygohere_cuzIaintgivingumine.:)' # get ur API key from hxxps://ipinfo[.]io/
INPUT_FILE = 'ips.txt'
OUTPUT_FILE = 'ips.csv'
DELAY_BETWEEN_REQUESTS = 1/2 #In seconds 1/2 = 0.5 sec


ips = []

with open(INPUT_FILE, "r") as file:
    file_contents = file.read()
    ips = file_contents.split("\n")


def get_ip_info(ip_passed: str = ""):
    response = requests.get(f'https://ipinfo.io/{ip_passed}/json?token={API_KEY}')
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data', 'status_code': response.status_code}

def append_csv(text_passed: str = "") -> bool:
    try:
        with open(OUTPUT_FILE, "a") as file:
            file.write(f"{text_passed}\n")
        return True
    except Exeption as ex:
        print(ex)
        return False

output = []
counter = 0
for ip in ips:
    info = get_ip_info(ip)
    counter += 1
    print(f"Counter: {counter},IP: {ip}, Location: {info.get('city', 'Unknown')}, {info.get('region', 'Unknown')}, {info.get('country', 'Unknown')}, Provider: {info.get('org', 'Unknown')}")

    output.append(f"{ip}|{info.get('hostname', 'Unknown')}|{info.get('city', 'Unknown')}|{info.get('region', 'Unknown')}|{info.get('country', 'Unknown')}|{info.get('loc', 'Unknown')}|{info.get('org', 'Unknown')}|{info.get('postal', 'Unknown')}|{info.get('timezone', 'Unknown')}")
    if append_csv(output[-1]) == False: exit()
    time.sleep(DELAY_BETWEEN_REQUESTS)

for i in output: print(output)
