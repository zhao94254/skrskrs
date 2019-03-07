#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2019-03-07 17:16
# @Author  : zpy
# @Software: PyCharm

# 定义数据结构，对结果进行检查

class SDict(dict):

    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)


class BaseModel:

    def __init__(self):
        pass

    def check(self):
        pass


if __name__ == '__main__':
    s = SDict()
    s.d = 2
    print(s)