import requests
raw_url = "https://raw.githubusercontent.com/Eluviian/CMPUT404Lab1/main/Lab1.py"

#print(requests.__version__)
#response = requests.get("https://google.com")
#print(response.text)

#source: https://stackoverflow.com/
#from page: https://stackoverflow.com/questions/64430181/how-to-access-the-github-api-via-requests-in-python
#user page:  https://stackoverflow.com/users/1581090/alex
headers = {"Accept": "application/vnd.github.inertia-preview+json"}
r = requests.get(raw_url, headers)

print(r.text)

