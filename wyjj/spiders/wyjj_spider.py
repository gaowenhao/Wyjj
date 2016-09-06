# encoding=utf-8
import scrapy
from scrapy import Request
from wyjj.items import WyjjItem
import re

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

        fund_item['week_increment'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_achive"]/table[@class="fn_cm_table"]/tbody/tr[1]/td[2]/span/text()').extract()

        fund_item['month_increment'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_achive"]/table[@class="fn_cm_table"]/tbody/tr[1]/td[3]/span/text()').extract()

        fund_item['season_increment'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_achive"]/table[@class="fn_cm_table"]/tbody/tr[1]/td[4]/span/text()').extract()

        fund_item['half_increment'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_achive"]/table[@class="fn_cm_table"]/tbody/tr[1]/td[5]/span/text()').extract()

        fund_item['year_increment'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_achive"]/table[@class="fn_cm_table"]/tbody/tr[1]/td[6]/span/text()').extract()

        fund_item['this_year_increment'] = response.xpath(
            '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_achive"]/table[@class="fn_cm_table"]/tbody/tr[1]/td[7]/span/text()').extract()

        list_asset_configuration = []

        #  资产配置注入值.
        for x in range(2, 6):
            variety = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_setup"]/table[@class="fn_cm_table fn_fund_config"]/tbody/tr[%s]/td[1]/text()' % x).extract()
            fund_amount = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_setup"]/table[@class="fn_cm_table fn_fund_config"]/tbody/tr[%s]/td[2]/text()' % x).extract()
            fund_ratio = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_setup"]/table[@class="fn_cm_table fn_fund_config"]/tbody/tr[%s]/td[2]/text()' % x).extract()
            list_asset_configuration.append("%s-%s-%s" % (variety, fund_amount, fund_ratio))

        fund_item['asset_configuration'] = list_asset_configuration

        list_heavy_stocks = []
        for x in range(1, 11):
            stock_name = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][1]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[1]/text()' % x).extract()
            if stock_name is None or len(stock_name) < 1:
                break
            elif re.match('^\s*', stock_name[0]):
                break
            stock_amount = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][1]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[2]/text()' % x).extract()
            market_value = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][1]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[3]/text()' % x).extract()
            stock_ratio = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][1]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[4]/text()' % x).extract()

            list_heavy_stocks.append('%s-%s-%s-%s' % (stock_name, stock_amount, market_value, stock_ratio))

        fund_item['stock_configuration'] = list_heavy_stocks

        list_heavy_business = []
        for x in range(2, 7):
            business = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][2]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[1]/text()' % x).extract()
            market_value = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][2]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[1]/text()' % x).extract()
            business_radio = response.xpath(
                '//div[@class="fn_wrap"]/div[@class="fn_fund_gird"][2]/div[@class="fn_fund_main fn_fund_infos"]/div[@class="fn_fund_invest"]/div[@class="fn_fund_mod_content"]/div[@class="fn_fund_invest_item"][2]/table[@class="fn_cm_table"]/tbody/tr[%s]/td[1]/text()' % x).extract()

            list_heavy_business.append("%s-%s-%s" % (business, market_value, business_radio))

        fund_item['industry_configuration'] = list_heavy_business

        yield fund_item

    def start_requests(self):
        for line in f:
            yield Request("http://quotes.money.163.com/fund/%s.html" % line.strip(),
                          headers={'User-Agent': "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"})
