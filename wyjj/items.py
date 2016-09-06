# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WyjjItem(scrapy.Item):
    name = scrapy.Field()  # 基金名
    code = scrapy.Field()
    dividend = scrapy.Field()  # 分红
    total_asset = scrapy.Field()  # 总净资产
    invest_type = scrapy.Field()  # 基金类型
    invest_style = scrapy.Field()  # 投资风格
    fund_manager = scrapy.Field()  # 基金经理
    fund_company = scrapy.Field()  # 基金公司
    establish_date = scrapy.Field()  # 建立时间

    week_increment = scrapy.Field()  # 周涨幅
    month_increment = scrapy.Field()  # 月涨幅
    season_increment = scrapy.Field()  # 季度涨幅
    half_increment = scrapy.Field()  # 半年涨幅
    year_increment = scrapy.Field()  # 年涨幅
    this_year_increment = scrapy.Field()  # 今年涨幅

    asset_configuration = scrapy.Field()  # 资产配置
    stock_configuration = scrapy.Field()  # 重仓持有股票
    industry_configuration = scrapy.Field()  # 重仓投资行业
