# Scrapy settings for basics project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'basics (+http://www.yourdomain.com)'

import sys

sys.path.insert(0, '/home/urkonn/prog/Python/projects/dofapi/dofapi')

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'dofapi.settings'

ITEM_PIPELINES = {
    'scraper.pipelines.PublicacionPipeline': 1000, 
    }
