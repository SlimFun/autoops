#!/usr/bin/env python
# encoding: utf-8

import sys
import pycurl

py3 = sys.version_info[0] > 2

class Test:
    def __init__(self):
        self.contents = ''
        if py3:
            self.contents = self.contents.encode('ascii')

    def body_callback(self,buf):
        self.contents = self.contents + buf

sys.stderr.write("Testing %s\n" % pycurl.version)

t = Test()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.baidu.com')
c.setopt(c.WRITEFUNCTION,t.body_callback)
c.perform()
c.close()

print(t.contents)
