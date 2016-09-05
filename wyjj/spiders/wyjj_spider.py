import scrapy
from scrapy import Request
from wyjj.items import WyjjItem

f = open('E:/moneywy/hhjj_2016_09_02.txt', 'r')


class MovieLinkSpider(scrapy.Spider):
    name = "wyjj"
    allowed_domains = ['money.163.com', '163.com']

    def parse(self, response):
        fund_item = WyjjItem()
        fund_item['code'] = response.url[-11:-5]
        fund_item['name'] = response.xpath('//div[@class="fn_wrap"]/div[@class="fn_data_title"]/h2/a/text()').extract()
        fund_item['dividend'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[1]/li[2]/span/text()').extract()
        fund_item['total_asset'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[1]/li[3]/span/text()').extract()
        fund_item['invest_type'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[1]/li[5]/span/text()').extract()
        fund_item['invest_style'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[1]/li[6]/span/text()').extract()
        fund_item['fund_manager'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[1]/li[7]/span/a/text()').extract()
        fund_item['fund_company'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[1]/li[8]/span/text()').extract()
        fund_item['establish_date'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_data_title"]/ul[2]/li[1]/span/text()').extract()



    def start_requests(self):
        for line in f:
            yield Request("http://quotes.money.163.com/fund/%s.html" % line.strip(),
                          headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"})
