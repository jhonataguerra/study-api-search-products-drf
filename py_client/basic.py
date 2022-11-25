import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything/"


get_response = requests.get(endpoint)  # Http Request
print(get_response.text)  # Print raw text response
