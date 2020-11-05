import requests

# HTML response
# resp = requests.get("https://www.baidu.com")
# print(resp.status_code)
#
# print(resp.encoding)
# print(resp.text)
# print(resp.content)
#
# resp.encoding = 'utf-8'
# print(resp.encoding)
# print(resp.text)
# print(resp.content)

# JSON response
# payload = {'key1': 'value1', 'key2': 'value2'}
# json_resp = requests.get("http://httpbin.org/get", params=payload)
#
# print(json_resp.status_code)
# print(json_resp.raise_for_status())
# print(json_resp.encoding)
#
# print(json_resp.text)
# print(json_resp.content)
#
# print(json_resp.json())
# print(json_resp.json().get('args'))

# RAW response
resp = requests.get('https://api.github.com/events', stream=True)
print(vars(resp.raw))
print(resp.raw.read(10))
print(resp.raw.headers)
