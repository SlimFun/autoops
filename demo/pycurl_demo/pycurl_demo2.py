#!/usr/bin/env python
# encoding: utf-8

import pycurl
import StringIO

c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://www.baidu.com')

b = StringIO.StringIO()

# 将pycurl获取的内容写入到StringIO缓存中
c.setopt(pycurl.WRITEFUNCTION,b.write)
c.perform()
print b.getvalue()
