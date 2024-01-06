import requests

for input in ["red","green","blue"]:
  response = requests.get("http://127.0.0.1:5000?input={input}")
  print(response)