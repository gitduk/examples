import json

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
get_resp = requests.get("http://httpbin.org/get", params=payload)
print(get_resp.url)
print(get_resp.text)

payload_2 = {'key1': 'value1', 'key2': ['value2', 'value3', 'value4']}
get_resp = requests.get("http://httpbin.org/get", params=payload_2)
print(get_resp.url)
print(get_resp.text)

post_resp = requests.post('http://httpbin.org/post', params=payload_2, data={'key': 'value'})
print(post_resp.text)
print(post_resp.headers)

payload_3 = (('key1', 'value1'), ('key1', 'value2'))
post_resp = requests.post("http://httpbin.org/post", data=payload_3)
print(post_resp.url)
print(post_resp.text)

payload_4 = {'some': 'data'}
post_resp = requests.post("https://api.github.com/some/endpoint", json=payload_4)
# post_resp = requests.post("https://api.github.com/some/endpoint", data=json.dumps(payload_4))
print(post_resp.text)
