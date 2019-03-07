#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2019-03-07 17:16
# @Author  : zpy
# @Software: PyCharm

# 定义数据结构，对结果进行检查

from exceptions import ModelError

class SDict(dict):

    def __getattr__(self, item):
        return self.get(item)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)


class BaseModel:

    def __init__(self, mds):
        """
        :param mds:[(sp, int), (ps, str)]
        """
        self.mds = mds
        self.mds_map = {}
        self.res = SDict()
        self.check()

    def _check_mds(self):
        for i in self.mds:
            if len(i) != 2:
                raise ModelError
            self.mds_map[i[0]] = i[1]
            if isinstance('str', i[1]):
                self.res[i[0]] = "NULL"
            elif isinstance(1, i[1]):
                self.res[i[0]] = -1
            elif isinstance(1.0, i[1]):
                self.res[i[0]] = -1.0

    def check(self):
        self._check_mds()

    def sql(self):
        return "insert into {table} {keys} values{}"


if __name__ == '__main__':
    # s = SDict()
    # s.d = 2
    # print(s)

    tmodel = BaseModel([('name', str), ('age', int)])
    tmodel.res.ks = 2
    print(tmodel.res)