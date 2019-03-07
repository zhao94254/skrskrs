#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2019-03-07 12:28
# @Author  : zpy
# @Software: PyCharm

from pspider import Pspider, req



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
    sp = SiteSpider()
    sp.start()
    print(sp.result)
