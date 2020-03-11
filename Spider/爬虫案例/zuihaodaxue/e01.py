from urllib import request
from lxml import etree
import time

base_url = 'http://zuihaodaxue.com/zuihaodaxuepaiming2019.html'

response = request.urlopen(base_url)
html =response.read().decode()
# print(html)

html = etree.HTML(html)

items = html.xpath('//tr[@class="alt"]')
# print(items)

# 若有文件清除
with open('zuihaodaxue.txt', 'w', encoding='utf-8') as f:
    pass

print('Starting....')
print(time.ctime())

for item in items:
    # 排名
    number = item.xpath('./td')[0].text
    if number == None:
        number = 'None'
    # 学校名称
    school = item.xpath('.//div[@align="left"]')[0].text
    if school == None:
        school = 'None'
    # 省份
    addr = item.xpath('./td')[2].text
    if addr == None:
        addr = 'None'
    # 总分
    score = item.xpath('./td')[3].text
    if score == None:
        score = 'None'
    # 生源质量（新生高考成绩得分）
    quality = item.xpath('.//td[@class="hidden-xs need-hidden indicator5"]')[0].text
    if quality == None:
        quality = 'None'
    # 培养结果（毕业生就业率）
    toe = item.xpath('.//td[@class="hidden-xs need-hidden indicator6"]')[0].text
    if toe == None:
        toe = 'None'
    # 社会声誉（社会捐赠收入·千元）
    donation  = item.xpath('.//td[@class="hidden-xs need-hidden indicator7"]')[0].text
    if donation == None:
        donation = 'None'
    # 科研规模（论文数量·篇）
    paper_num = item.xpath('.//td[@class="hidden-xs need-hidden indicator8"]')[0].text
    if paper_num == None:
        paper_num = 'None'
    # 科研质量（论文质量·FWCI）
    paper_quality = item.xpath('.//td[@class="hidden-xs need-hidden indicator9"]')[0].text
    if paper_quality == None:
        paper_quality = 'None'
    # 顶尖成果（高被引沦为·篇）
    hot_paper = item.xpath('.//td[@class="hidden-xs need-hidden indicator10"]')[0].text
    if hot_paper == None:
        hot_paper = 'None'
    # 顶尖人才（ 高被引学者·人）
    hot_people = item.xpath('.//td[@class="hidden-xs need-hidden indicator11"]')[0].text
    if hot_people == None:
        hot_people = 'None'
    # 科技服务（企业科研经费·千元）
    funds = item.xpath('.//td[@class="hidden-xs need-hidden indicator12"]')[0].text
    if funds == None:
        funds = 'None'
    # 成果转化（技术转让收入·千元）
    transfer_money = item.xpath('.//td[@class="hidden-xs need-hidden indicator13"]')[0].text
    if transfer_money == None:
        transfer_money = 'None'
    # 学生国际化（留学生比例）
    proportion = item.xpath('.//td[@class="hidden-xs need-hidden indicator14"]')[0].text
    if proportion == None:
        proportion = 'None'

    with open('zuihaodaxue.txt', 'a', encoding='utf-8') as f:
        text = number + ' - ' + school + ' - ' + addr + ' - ' + score + ' - ' + quality + ' - ' + toe + ' - ' + \
            donation + ' - ' + paper_num + ' - ' + paper_quality + ' - ' + hot_paper + ' - ' + hot_people + \
            ' - ' + funds + ' - ' + transfer_money + ' - ' + proportion
        f.write(text + '\n')

print('ending...')
print(time.ctime())