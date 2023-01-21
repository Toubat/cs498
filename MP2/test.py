import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
    'ip_address1':  '18.222.99.81:5000',
    'ip_address2':  '3.138.111.184:5000',
    'load_balancer':  'cs498-mp2-1922177236.us-east-2.elb.amazonaws.com',
    'submitterEmail':  'toubatbrian@gmail.com',
    'secret': 'sls4zkj5t6DFERow'
}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)