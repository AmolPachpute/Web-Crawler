# -*- coding: utf-8 -*-

# Scrapy settings for Docomo_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# http://www.plansinfo.com/tata-docomo.html

BOT_NAME = 'Docomo_crawler'

SPIDER_MODULES = ['Docomo_crawler.spiders']
NEWSPIDER_MODULE = 'Docomo_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Docomo_crawler (+http://www.yourdomain.com)'
