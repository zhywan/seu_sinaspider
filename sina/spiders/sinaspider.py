# -*- coding: utf-8 -*-
import scrapy
import time,re
# from selenium import webdriver
from items import SinaItem,SinaItemloader,processcook
from urllib import parse

class SinaspiderSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'sina.pipelines.SinaPipeline': 100, },
    }

    name = 'sinaspider'
    flag=0
    allowed_domains = ['www.weibo.com']
    # start_urls = ['http://weibo.com/liuyifeiofficial?profile_ftype=1&is_all=1#_0']
    # headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0" }
    def __init__(self,cookie,url,**kwargs):
        # chromeOptions = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chromeOptions.add_experimental_option("prefs", prefs)
        # self.browser = webdriver.Chrome(executable_path="D:/chromedriver.exe",chrome_options=chromeOptions)
        #     # self.browser.add_cookie(cook)
        print(cookie)
        self.starturl=url
        self.oldcook = cookie
        self.cook=processcook(cookie)
    def parse(self, response):
        # Sina_Item = SinaItem()
        # # likenum=response.xpath("//div[@tbinfo]//div[@class='WB_feed_handle']//em[contains(@class, 'W_ficon') and contains(@class, 'ficon_praised')]/following-sibling::em").extract()
        # # repeatnum=response.xpath("//div[@tbinfo]//div[@class='WB_feed_handle']//em[contains(@class, 'W_ficon') and contains(@class, 'ficon_forward')]/following-sibling::em").extract()
        # # commentnum=response.xpath("//div[@tbinfo]//div[@class='WB_feed_handle']//em[contains(@class, 'W_ficon') and contains(@class, 'ficon_repeat')]/following-sibling::em").extract()
        #
        #
        #
        #
        # nextpage=response.xpath("//div[@class='W_pages']/span/following-sibling::a/text()").extract()
        # # nexturl_part=response.xpath("//div[@class='W_pages']/span/following-sibling::a/@href").extract()[0]
        # # nexturl= parse.urljoin(response.url, nexturl_part)
        # item_loader = SinaItemloader(item=SinaItem(),response=response)
        # item_loader.add_value('cookie',self.settings.get("COOKIE"))
        # item_loader.add_xpath('datetime',"//div[@tbinfo]//div[@class='WB_detail']/div[contains(@class,'WB_from') and contains(@class,'S_txt2')]/a[1]/text()")
        # item_loader.add_xpath('likenum',"//div[@tbinfo]/div[@class='WB_feed_handle']//em[contains(@class, 'W_ficon') and contains(@class, 'ficon_praised')]/following-sibling::em/text()")
        # item_loader.add_xpath('repeatnum',"//div[@tbinfo]/div[@class='WB_feed_handle']//em[contains(@class, 'W_ficon') and contains(@class, 'ficon_forward')]/following-sibling::em/text()")
        # item_loader.add_xpath('commentnum',"//div[@tbinfo]/div[@class='WB_feed_handle']//em[contains(@class, 'W_ficon') and contains(@class, 'ficon_repeat')]/following-sibling::em/text()")
        # Sina_Item=item_loader.load_item()
        # yield Sina_Item
        # if nextpage:
        #     nexturl_part = response.xpath("//div[@class='W_pages']/span/following-sibling::a/@href").extract()[0]
        #     nexturl = parse.urljoin(response.url, nexturl_part)
        #     yield scrapy.Request(nexturl,dont_filter=True,callback=self.parse)

        sina_item=SinaItem()
        all=response.xpath('//div[@class="c"]//div[last()]').extract()
        alltime=response.xpath('//div[@class="c"]//span[@class="ct"]/text()').extract()
        result=re.search(r"(.*)来自",alltime[1])[1]
        for i in range(len(all)):
            sina_item["likenum"]=re.search(r"赞\[(\d+)\]",all[i])[1]
            sina_item["repeatnum"]=re.search(r"转发\[(\d+)\]",all[i])[1]
            sina_item["commentnum"]=re.search(r"评论\[(\d+)\]",all[i])[1]
            sina_item["datetime"] =result=re.search(r"(.*)\xa0来自",alltime[i])[1]
            sina_item["cookie"] = result = self.oldcook
            yield sina_item


    def start_requests(self):
        # chromeOptions = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chromeOptions.add_experimental_option("prefs", prefs)
        # self.browser = webdriver.Chrome(executable_path="D:/chromedriver.exe", chrome_options=chromeOptions)
        # # self.browser = webdriver.PhantomJS(executable_path="D:/seu_sinaspider/phantomjs/bin/phantomjs.exe")
        # yield scrapy.Request('https://www.weibo.com/',callback=self.loginsina)
        # print(self.settings.get("COOKIE"))
        # self.cook = processcook(self.settings.get("COOKIE"))

        # print(self.cook)
        # print(self.starturl)
        yield scrapy.Request("https://weibo.cn/u/"+self.starturl,cookies=self.cook,callback=self.generate_page)

    def generate_page(self,response):
        total=response.xpath('//*[@id="pagelist"]/form/div/text()').extract()[1].strip()
        result=re.search("(\d+)/(\d+)",total)
        total=int(result[2])
        print(total)
        for i in range(total):
            url="https://weibo.cn/" + self.starturl+"?page="+str(i+1)
            yield scrapy.Request(url, dont_filter=True,cookies=self.cook,callback=self.parse)

    # def loginsina(self,response):
    #     # time.sleep(10)
    #     # username = self.browser.find_element_by_xpath('//*[@id="loginname"]')
    #     # password = self.browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
    #     # login = self.browser.find_element_by_xpath('''//*[@id="pl_login_form"]/div/div[3]/div[6]/a''')
    #     # username.send_keys("1131894367@qq.com")  # 此处填入用户名
    #     # password.send_keys("laijingzhi")  # 此处填入密码
    #     # login.click()
    #     # time.sleep(15)
    #     # self.flag=1
    #     # for url in self.start_urls:
    #     #     yield scrapy.Request(url,dont_filter=True,callback=self.parse)
    #     # a = (self.settings.get("COOKIE_URL").split('|')[0]).split(";")
    #     cook=self.settings.get("COOKIE").split(";")
    #     result_dic = {}
    #     for each in cook:
    #         result_dic = {'domain': '.weibo.com', 'httpOnly': False, 'path': '/', 'secure': False, }
    #         result = each.split("=")
    #         result_dic['name'] = result[0].strip()
    #         result_dic['value'] = result[1].strip()
    #         self.browser.add_cookie(result_dic)
    #     self.flag = 1
    #     yield scrapy.Request(self.settings.get("URL"), dont_filter="true",callback=self.parse)
    #

