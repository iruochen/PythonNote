from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/972301090/profile"

    headers = {
        "Cookie": "anonymid=k0t4cq4s5whzwg; depovince=SX; jebecookies=254aff72-33ce-4da5-840c-2a285d3e6a30|||||; _r01_=1; JSESSIONID=abcEg3t1ZLigH-9Bsus1w; ick_login=19410208-7d7a-442a-858b-c996155af213; _de=92A46B3E308785D3496B0B0F305EAFFF; p=b9a464ff4ad809f2f9e718c0bf2b316f0; first_login_flag=1; ln_uact=18203503747; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=455fae39c10094e5cd41ef42f092b6370; societyguester=455fae39c10094e5cd41ef42f092b6370; id=972301090; xnsid=adae9600; loginfrom=syshome; jebe_key=691baa31-674d-4088-86fd-a44c6049ebb4%7Ce3fb613f795528462326e4d7ae14d876%7C1569044131586%7C1%7C1569044137500; jebe_key=691baa31-674d-4088-86fd-a44c6049ebb4%7Ce3fb613f795528462326e4d7ae14d876%7C1569044131586%7C1%7C1569044137503; wp_fold=0"
    }

    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    with open("rsp.html", "w", encoding='utf-8') as f:
        f.write(html)