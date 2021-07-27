import requests, pytest

def requestGet(url, params, headers):
    return requests.get(url=url, params=params, headers=headers)

def responseGetKey(url, params, headers):
    return requestGet(url, params, headers).json()[0]["is_watched"]

def testDoubanPaihang():
    Url = "https://movie.douban.com/j/chart/top_list?"
    param = {
        "type": "24",
        "interval_id": "100:90",
        "action": "",
        "start": "0",  # 从库中的第几部电影开始取
        "limit": "20"   # 一次取出电影的数量
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    assert responseGetKey(Url, param, headers) == False

if __name__ == '__main__':
    pytest.main()