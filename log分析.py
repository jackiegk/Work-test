#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import codecs

f1 = open('1.txt', 'r',encoding="utf8")
f2 = open('2.txt', 'w',encoding="utf8")

result = list()
for line in open('1.txt',encoding="utf8"):
    flag = f1.readline()
    if "加载素材file"in flag:
        f2.write(line)
    if "素材彻底释放完毕：Test" in flag:
        f2.write(line+ '\n')
