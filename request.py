import requests


body = {
  "anythingiwant": {
    "nestedkey": "nestedvalue"
    }
  }


response = requests.post("https://gabrielcollitestg.azurewebsites.net/api/HttpTrigger1", json=body)
print(response.text)
    