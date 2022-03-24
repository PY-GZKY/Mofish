import requests

ip_api = "http://httpbin.org/get"
ip_info_api = "http://ip-api.com/json/{}?lang=zh-CN"
w_api = "http://wthrcdn.etouch.cn/weather_mini?city={}"

headers = {

}


def get_w():
    r = requests.session()
    return r.get(url=w_api.format(r.get(url=ip_info_api.format(r.get(url=ip_api, headers=headers).json().get("origin")),
                                        headers=headers).json().get("city")), headers=headers).json()


# print(get_w())
