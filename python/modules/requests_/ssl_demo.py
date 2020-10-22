import requests

url = "https://cn.bing.com/search?q=%E9%9C%80%E8%A6%81ssl%E9%AA%8C%E8%AF%81%E7%9A%84%E7%BD%91%E9%A1%B5&qs=n&form=QBLH&sp=-1&pq=%E9%9C%80%E8%A6%81ssl%E9%AA%8C%E8%AF%81%E7%9A%84%E7%BD%91%E9%A1%B5&sc=0-10&sk=&cvid=B0545785836C4840AE56C8CB0070C3ED"

with requests.session() as s:
    resp = s.get(url, verify=True)
    print(f"resp: {resp}")
