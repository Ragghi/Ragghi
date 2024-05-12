# Python
# requires Requests
# pip install requests

import requests

apiKey = "qil5PskQL0ig4elyoQszsQ"  # TODO: Replace with your API key

codigo = "codigo"  # TODO: Replace with your value

url = "https://sai-library.saiapplications.com"
headers = {"X-Api-Key": apiKey}
data = {
    "inputs": {
        "codigo": codigo,
    }
}

response = requests.post(f"{url}/api/templates/65242502b451fe561dfa738d/execute", json=data, headers=headers)
if response.status_code == 200:
    print(response.text)