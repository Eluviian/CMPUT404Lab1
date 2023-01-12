import requests
raw_url = "https://raw.githubusercontent.com/Eluviian/CMPUT404Lab1/main/Lab1.py"

#print(requests.__version__)
#response = requests.get("https://google.com")
#print(response.text)

headers = {"Accept": "application/vnd.github.inertia-preview+json"}
r = requests.get(raw_url, headers)

print(r.text)

