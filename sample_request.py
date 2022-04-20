import requests



res = requests.get("https://petstore.swagger.io/v2/swagger.json")
response_body = res.json()
print(response_body)
