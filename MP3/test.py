import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
	"graphApi": 'https://4s4zr56ibd.execute-api.us-east-1.amazonaws.com/prod/graph',
	"botName": 'QueryDistanceBot',
	"botAlias": 'query_distance_bot',
	"identityPoolId": 'us-east-1:4f4cd8ec-de47-473d-8312-34c8080f41ae',
	"accountId": '442740141882',
	"submitterEmail": 'toubatbrian@gmail.com',
	"secret": 'rb56ezYW02HIpLNr',
	"region": 'us-east-1',
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)