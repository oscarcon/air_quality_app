# -*- coding: utf-8 -*-
import scrapy
import re

class CrawlEverthingSpider(scrapy.Spider):
    name = 'crawl_everthing'
    allowed_domains = ['https://vieclam24h.vn/tim-kiem-viec-lam-nhanh/?hdn_nganh_nghe_cap1=']
    start_urls = ['https://vieclam24h.vn/tim-kiem-viec-lam-nhanh/?hdn_nganh_nghe_cap1=&hdn_dia_diem=&hdn_tu_khoa=&hdn_hinh_thuc=&hdn_cap_bac=']
    
    def parse(self, response):
        XPATH = '//div[@title="Mức lương"]/text()'
        for salary in response.xpath(XPATH):
            processed_salary = salary.get().replace('\n','')
            processed_salary = processed_salary.strip()
            processed_salary = re.sub(' +', ' ', processed_salary)
            print(processed_salary)

