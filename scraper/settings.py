# Scrapy settings for basics project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

## Basado en https://github.com/CodeandoMexico/web-scraping

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'basics (+http://www.yourdomain.com)'
import os
import sys

sys.path.insert(0, '/home/user/.../dofapi/dofapi')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dofapi.settings'

ITEM_PIPELINES = {
    'scraper.pipelines.PublicacionPipeline': 1000, 
    }
