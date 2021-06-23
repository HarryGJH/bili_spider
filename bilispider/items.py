# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilispiderItem(scrapy.Item):
    # define the fields for your item here like:
    index_show=scrapy.Field()   #集数
    is_finish=scrapy.Field()    #是否完结
    link=scrapy.Field()         #链接
    media_id=scrapy.Field()     #视频id
    season_id=scrapy.Field()    #id
    order=scrapy.Field()        #播放量
    title=scrapy.Field()        #标题
    coins=scrapy.Field()        #投币数量
    danmakus=scrapy.Field()     #弹幕数量
    likes=scrapy.Field()        #点赞数量
    follow=scrapy.Field()       #追剧数量
    views=scrapy.Field()        #观看数量