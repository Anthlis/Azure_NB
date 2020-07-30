import requests
import pprint as pprint
import json
from datetime import datetime

response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)

pprint.pprint(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())

parameters = {
    "lat": 43.5908,
    "lon": 172.3792
}

resp2 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
jprint(resp2.json())

pass_times = resp2.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

times= []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

for time in times:
    if time.hour > 12:
        print(f"Look for the ISS at {time.hour}:{time.minute}:{time.second}")
    else:
        print(f"{time.year}-{time.month}-{time.day}, 'NZ Daytime Pass'")