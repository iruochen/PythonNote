'''
破解有道词典
V1
'''

from urllib import request, parse

def youdao(key):

    # url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        "i": "boy",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15690523207222",
        "sign": "1e28e83873cd4690e108ea28350cd4bb",
        "ts": "1569052320722",
        "bv": "a4f4c82afd8bdba188e568d101be3f53",
        "doctype": "json",
        "version": "2.1"
    }

    # 参数data需要时bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application / json, text / javascript, * / *; q = 0.01",
        # "Accept - Encoding": "gzip, deflate",
        "Accept - Language": "zh - CN, zh;q = 0.9",
        "Connection": "keep - alive",
        "Content - Length": "237",
        "Content - Type": "application / x - www - form - urlencoded;charset = UTF - 8",
        "Cookie": "OUTFOX_SEARCH_USER_ID = -1916336379 @ 10.169.0.84;JSESSIONID = aaaF3jqgNCov6fQWqZs1w;OUTFOX_SEARCH_USER_ID_NCOO = 885890211.5426716;___rl__test__cookies = 1569052795328",
        "Host": "fanyi.youdao.com",
        "Origin": "dhttp: // fanyi.youdao.com",
        "Referer": "http: // fanyi.youdao.com/",
        "User - Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.132Safari / 537.36",
        "X - Requested - With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("boy")