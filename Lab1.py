import requests

print(requests.__version__)
response = requests.get("https://google.com")
print(response.text)