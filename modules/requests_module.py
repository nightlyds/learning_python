import requests

requests_site = requests.get("https://docs.python-requests.org/en/master/user/quickstart/")

print(f"Text {requests_site.text}")
print(f"Content {requests_site.content}")
print(f"Status code {requests_site.status_code}")
print(f"Headers {requests_site.headers}")

# Auth: requests.get('https://api.github.com/user', auth=('user', 'pass'))