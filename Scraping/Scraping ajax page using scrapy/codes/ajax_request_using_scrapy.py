# -*- coding: utf-8 -*-
import sys
import locale
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.http import Request, HtmlResponse
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from lxml import etree
from BeautifulSoup import BeautifulSoup
import json
import codecs
import csv
from collections import defaultdict, OrderedDict
import requests
import urllib


def dict_2_Body_Form(form_data, boundary):
    payload_ = []
    for k, v in form_data.items():
        payload_.append("--"+boundary)
        payload_.append('Content-Disposition: form-data; name="%s"' % k)
        payload_.append('')
        payload_.append(v)
    payload_.append("--"+boundary+"--")
    # payload_.append('')

    return "\r\n".join(payload_)


class EsquireAjaxSpider(scrapy.Spider):
    name = 'news_ajaxscraper'    
    allowed_domains = ['esquire.kz']

    def start_requests(self):
    	# 1
    	# Ajax url
    	api_url="https://esquire.kz/wp-admin/admin-ajax.php"

        # 2.1
        # request header
    	my_boundary = "tikiskenski"   # can be anything
        my_headers = {'content-type': "multipart/form-data; boundary=%s" % my_boundary}

        # 2.2
        # get params into body form string
        form_data = {"action": "loadmore"
                    ,"query" : """{"category_name":"lifestyle","error":"","m":"","p":0,"post_parent":"","subpost":"","subpost_id":"","attachment":"","attachment_id":0,"name":"","static":"","pagename":"","page_id":0,"second":"","minute":"","hour":"","day":0,"monthnum":0,"year":0,"w":0,"tag":"","cat":241,"tag_id":"","author":"","author_name":"","feed":"","tb":"","paged":0,"meta_key":"","meta_value":"","preview":"","s":"","sentence":"","title":"","fields":"","menu_order":"","embed":"","category__in":[],"category__not_in":[],"category__and":[],"post__in":[],"post__not_in":[],"post_name__in":[],"tag__in":[],"tag__not_in":[],"tag__and":[],"tag_slug__in":[],"tag_slug__and":[],"post_parent__in":[],"post_parent__not_in":[],"author__in":[],"author__not_in":[],"ignore_sticky_posts":false,"suppress_filters":false,"cache_results":true,"update_post_term_cache":true,"lazy_load_term_meta":true,"update_post_meta_cache":true,"post_type":"","posts_per_page":13,"nopaging":false,"comments_per_page":"50","no_found_rows":false,"order":"DESC"}"""
                    ,"page"  : "0"}
        body_form = dict_2_Body_Form(form_data, my_boundary)  # i.e i.e. payload


        # 3
        # start sending ajax requests to get pages
        yield scrapy.FormRequest(api_url
                                 ,body= body_form
                                 ,method="POST"
                                 ,headers=my_headers
                                 ,callback=self.parse
                                 )


    def parse(self, response):
    	print response.body


if __name__=="__main__":
    process = CrawlerProcess()
    process.crawl(EsquireAjaxSpider)
    process.start()

