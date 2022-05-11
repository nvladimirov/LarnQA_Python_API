import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first = response.history[0]
second = response.history[1]
third = response

print(first.url)
print(second.url)
print(third.url)

