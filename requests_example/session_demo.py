import requests
from requests.utils import cookiejar_from_dict

url = "https://cn.bing.com/"
cookie_str = "_ga=GA1.2.936720431.1598431409; _gauges_unique_year=1; _gauges_unique=1; __cfduid=de1181724e35f5c5535289fadf3ccf80b1602465671; _gid=GA1.2.327549174.1602465674"
cookie_dict = dict([var.split('=', 1) for var in cookie_str.split(';')])

with requests.session() as s:
    s.headers = {"header": "12345678"}
    s.cookies = cookiejar_from_dict(cookie_dict)
    resp = s.get(url)

    print(resp.status_code)
    print(resp.headers)

    print(resp.request.url)
    print(resp.request.headers)

    print(s.cookies)
