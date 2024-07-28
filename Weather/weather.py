import requests

def get_wether(keyword):
    url = f"https://www.weather.go.kr/w/renew2021/rest/main/place-search.do?query={keyword}&start=1&src=A2"
    r = requests.get(url)
    _json = r.json()
    print(_json)


if __name__ == "__main__":
    get_wether("서울")