import requests
import csv
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.100 Safari/537.36'
}

r = requests.get('http://www.seputu.com', headers=headers)

html = etree.HTML(r.text)

div_mulus = html.xpath('//*[@class="mulu"]')

rows = []
for div_mulu in div_mulus:
    # 找h2标记
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    # print(div_h2)
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            # 找href属性
            href = a.xpath('./@href')[0]
            # 找子标题 title
            box_title = a.xpath('./@title')[0]
            # print(href, box_title)
            # print(type(box_title))

            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1)
                real_title = match.group(2)
                # print(date, real_title)
                content = (h2_title, real_title, href, date)
                rows.append(content)

headers = ['title', 'real_title', 'href', 'date']
with open('gcd.csv', 'a', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
