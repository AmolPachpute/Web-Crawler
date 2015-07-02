import scrapy
import ipdb
#from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import csv
class DocomoSpider(scrapy.Spider):
    name = "docomo_plans"
    allowed_domains = ["plansinfo.com"]
    start_urls = [
        "http://www.plansinfo.com/tata-docomo-prepaid-karnataka-plans.html"
    ]

    def parse(self, response):

        filename = response.url.split("/")[-2] + '.html'
        plans_list = [str(i) for i in response.selector.xpath("//h3/text()").extract()[:6]]
        titles_list = [str(i) for i in response.selector.xpath("//table/tr/th/b/text()").extract()[0:4]]
        file_obj = open(str(plans_list[0] + ".csv"), "wb")


        writer_obj = csv.writer(file_obj, delimiter=",")
        writer_obj.writerow([plans_list[0]])
        writer_obj.writerow(titles_list)


        ipdb.set_trace()
        for table_row in response.selector.xpath("//table[1]//tr").extract():
            row_response_object = HtmlResponse(url="", body=str(table_row))
            list1 = [str(i) for i in row_response_object.selector.xpath("//td/text()").extract()]
            writer_obj.writerow(list1)
        file_obj.close()






