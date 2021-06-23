import scrapy
import json
import copy
from scrapy.item import ItemMeta
from ..items import BilispiderItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ["api.bilibili.com"]
    pages=1
    start_urls = ["https://api.bilibili.com/pgc/season/index/result?page={}&season_type=3&pagesize=20&type=1".format(pages)]
    
    seasonurl=""
    mediaurl=""

    def parse(self, response):
        item=BilispiderItem()
        data_list=json.loads(response.text).get('data').get('list')
        # print(data_list)
        
        for data in data_list:
            item['index_show']=data['index_show']
            item['is_finish']='已完结' if data['is_finish']==1 else '未完结'
            item['link']=data['link']
            item['media_id']=data['media_id']
            item['order']=data['order']
            item['title']=data['title']
            item['season_id']=data['season_id']
            self.seasonurl="https://api.bilibili.com/pgc/web/season/stat?season_id="+str(data['season_id'])
            yield scrapy.Request(url=self.seasonurl,
                                callback=self.ratingParse,
                                meta={'item':copy.deepcopy(item)},
                                dont_filter=False)

        #下一页的请求
        if self.pages<5:
            self.pages+=1
            yield scrapy.Request(url="https://api.bilibili.com/pgc/season/index/result?page={}&season_type=3&pagesize=20&type=1".format(self.pages),
                                callback=self.parse)

    def ratingParse(self,response):
        item=response.meta['item']
        data=json.loads(response.text).get('result')
        item['coins']=data['coins']
        item['danmakus']=data['danmakus']
        item['likes']=data['likes']
        item['follow']=data['follow']
        item['views']=data['views']
        yield item
