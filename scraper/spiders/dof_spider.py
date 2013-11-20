from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scraper.items import PublicacionItem

class DofSpider(BaseSpider):
    name = "dof"
    allowed_domains = ["dof.gob.mx"]
    start_urls = [
        "http://www.dof.gob.mx/index.php"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        references = hxs.select('//a[@class="enlaces"]')
        notes = []
        for reference in references:
            note = PublicacionItem()
            note['description'] = reference.select('text()').extract()
            note['link'] = reference.select('@href').re('nota_detalle\.php.*')
            # Use only if link matches the previous regex
            if note['link']:
                notes.append(note)
        return notes
