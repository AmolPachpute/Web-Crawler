import scrapy
import ipdb
#from scrapy.selector import Selector
class DocomoSpider(scrapy.Spider):
    name = "docomo_plans"
    allowed_domains = ["plansinfo.com"]
    start_urls = [
        "http://www.plansinfo.com/tata-docomo-prepaid-karnataka-plans.html"
    ]

    def parse(self, response):
        ipdb.set_trace()
        filename = response.url.split("/")[-2] + '.html'
        plans_list = [str(i) for i in response.selector.xpath("//h3/text()").extract()[:6]]
        titles_list = [str(i) for i in response.selector.xpath("//table/tr/th/b/text()").extract()[0:4]]


        with open(filename, 'wb') as f:
            f.write(response.body)