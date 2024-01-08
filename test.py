import requests
import os

if os.environ.get("ENV_NAME") == "local":
  for input in ["red","green","blue"]:
    response = requests.get(f"http://127.0.0.1:5000?input={input}")
    print(response)
else:
  for input in ["red","green","blue"]:
    response = requests.get(f"https://amitapppod-service-amit-{os.environ.get('ENV_NAME')}.apps.opc-sonf-ogn.orange-guinee.com/?input={input}")
    print(response)
