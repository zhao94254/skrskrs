#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2019-03-06 17:19
# @Author  : zpy
# @Software: PyCharm

import abc
from abc import ABCMeta


class Pspider(metaclass=ABCMeta):

    @abc.abstractmethod
    def task(self):
        pass

    @abc.abstractmethod
    def req_resp(self):
        pass

    def start(self):
        pass