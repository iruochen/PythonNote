import requests
import re
import time
class Spider():
    url='https://www.douyu.com/g_LOL'
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT'
                 ' 10.0; Win64; x64) AppleWebKi'
                 't/537.36 (KHTML, like Gecko) '
                 'Chrome/64.0.3282.140 Safari/537.3'
                 '6 Edge/18.17763'}
    root_pattern='<div class="DyListCover' \
                 '-info">[\s\S]*?</h2></div>'
    name_pattern='<use xlink:href="#icon-user_c95a' \
                 'cf8"></use></svg>(.*?)</h2></div>'
    number_pattern='<use xlink:href="#icon-hot_8a57f0b"></' \
                   'use></svg>(.*?)</span>'



    def __fetchcontent(self,url):
        htmls=requests.get(url,headers=Spider.headers)
        htmls=htmls.text
        return htmls

    def _analysis(self,htmls):
        root_html=re.findall(Spider.root_pattern,htmls)

        anchors=[]
        for html in root_html:
            name=re.findall(Spider.name_pattern,html)
            number=re.findall(Spider.number_pattern,html)
            anchor={'name':name,'number':number}
            anchors.append(anchor)

        return anchors

    def __refine(self,anchors):
        l=lambda anchor:{'name':anchor['name'][0].strip(),
                         'number':anchor['number'][0]
                         }
        return map(l,anchors)

    def __sort(self,anchors):
         anchors=sorted(anchors,key=self.__sort_seed,reverse=True)
         return anchors

    def __sort_seed(self,anchor):
        r=re.findall('\d*',anchor['number'])
        number=float(r[0])
        if '万' in anchor['number']:
            number*=10000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print('rank '+str(rank+1)+' : '+
                  anchors[rank]['name']+'~~~~~~'
                  +anchors[rank]['number'])

    def  __promote(self,url):
        htmls = self.__fetchcontent(url)
        anchors = self._analysis(htmls)
        anchor = self.__refine(anchors)
        anchors = self.__sort(anchor)
        self.__show(anchors)
        time.sleep(3)

    def __listss(self):
        lists = ['LOL', 'jdqs', 'wzry', 'DOTA2', 'wzrpg', 'hpjy', 'TVgame', 'CF', 'ecy']
        return lists

    def __circle(self):

        for list in self.__listss():
            url = 'https://www.douyu.com/g_' + list
            print(url)
            self.__promote(url)


    def go(self):
        self.__circle()

spider=Spider()
spider.go()

