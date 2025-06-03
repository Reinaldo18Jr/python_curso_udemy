# requests para requisições HTTP
# pip install requests types-requests

# http://  -> porta 80
# https:// -> porta 443

import requests

url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
print(response.headers)
print(response.content)
print(response.text)
print(response.json())
