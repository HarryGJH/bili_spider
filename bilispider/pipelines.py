# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook
from scrapy.utils.project import get_project_settings
settings=get_project_settings()

class BilispiderPipeline:
    excel=Workbook()
    active=excel.active
    active.column_dimensions['A'].width=35
    active.column_dimensions['B'].width=11
    active.column_dimensions['C'].width=14
    active.column_dimensions['D'].width=10
    active.column_dimensions['E'].width=50
    active.column_dimensions['F'].width=12
    active.column_dimensions['G'].width=12
    active.column_dimensions['H'].width=12
    active.column_dimensions['I'].width=12
    active.column_dimensions['J'].width=12
    file=['标题','视频id','集数','是否完结','视频连接','投币数量','弹幕数量','点赞数量','追剧数量','观看数量']
    active.append(file)

    def process_item(self, item, spider):
        files =[item['title'],item['media_id'],item['index_show'],item['is_finish'],item['link'],
                item['coins'],item['danmakus'],item['likes'],item['follow'],item['views']
                ]
        self.active.append(files)
        self.excel.save('../../bilibili.xlsx')
        return item
