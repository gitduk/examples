import requests
from requests.utils import cookiejar_from_dict

url = 'http://httpbin.org/cookies'

cookies = dict(cookie_are="im a cookie")
resp = requests.get(url, cookies=cookies)
print(f"resp cookies: {resp.cookies} \nreq cookies: {resp.request._cookies}")

jar = requests.cookies.RequestsCookieJar()
jar.set("key", "value1", domain='httpbin.org', path='/cookies')
jar.set("key", "value2", domain='httpbin.org', path='/others')
resp = requests.get(url, cookies=jar)
print(f"resp cookies: {resp.text} \nreq cookies: {resp.request._cookies}")

cookies = dict(cookie='im an other cookie')
resp = requests.get(url, cookies=requests.utils.cookiejar_from_dict(cookies))
print(f"resp cookies: {resp.text} \nreq cookies: {resp.request._cookies}")