# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#class BasicsPipeline(object):
#    def process_item(self, item, spider):
#        return item

from apiapp.models import Publicacion

class PublicacionPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
