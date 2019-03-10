#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2019-03-07 12:28
# @Author  : zpy
# @Software: PyCharm

from spider.pspider import Pspider, req
from spider.model import BaseModel

class LagouSpider(Pspider):

    def task(self):
        return "https://www.lagou.com/zhaopin/Python/"

    def req_resp(self):

        @req()
        def pages():
            url = self.task()
            return {"request": {
                'url': url,
            },
                "response": {
                    "handler": self.parse_data,
                }}
        yield pages

    def parse_data(self, resp):
        lmodel = BaseModel([('company', str), ('companyid', str), ('positionname', str), ('salary', str), ('require', str)])
        for d in resp.html.xpath('//*[@id="s_position_list"]/ul/li'):
            lmodel.res.require = ''.join(d.xpath('//div[1]/div[1]/div[2]/div/text()'))
            lmodel.res.company = d.attrs.get('data-company')
            lmodel.res.companyid = d.attrs.get('data-companyid')
            lmodel.res.salary = d.attrs.get('data-salary')
            lmodel.res.positionname = d.attrs.get('data-positionname')
            lmodel.save()
        return lmodel

class SiteSpider(Pspider):

    def task(self):
        return "https://www.97up.cn"

    def req_resp(self):

        @req()
        def first_page():
            url = self.task()
            return {"request":{
                    'url': url,
                },
                "response":{
                    "handler": self.parse_data,
                }}
        yield first_page

    def parse_data(self, resp):
        html = resp.content
        return 'skr'

if __name__ == '__main__':
    sp = LagouSpider()
    sp.start()
    for wdata in sp.result:
        for s in wdata.export_sql('test.test'):
            print(s)
        wdata.export_csvfile('/Users/mioji/Desktop/newpy/pspider/example/lagoutest.csv')