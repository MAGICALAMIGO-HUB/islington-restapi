import requests

# endpoints2 = "https://httpbin.org/status/200"
# endpoints = "https://httpbin.org/anything"

# get_response = requests.get(endpoints,json ={"anish":"Hello World"})
# print(get_response.text)
# print(get_response.json())
# get_response = requests.get(endpoints2)
# print(get_response.status_code)
endpoints = "http://localhost:8000/api"

get_response = requests.get(endpoints)
print(get_response.text)