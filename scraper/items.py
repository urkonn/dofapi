# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#from scrapy.item import Item, Field

#class NoteItem(Item):
#    description = Field()
#    link = Field()

from scrapy.contrib_exp.djangoitem import DjangoItem
from apiapp.models import Publicacion

class PublicacionItem(DjangoItem):
    django_model = Publicacion
