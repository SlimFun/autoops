#!/usr/bin/env python
# encoding: utf-8

import sys
import pycurl
import time

class Test(object):
    def __init__(self):
        self.contents = ''

    def body_callback(self,buf):
        self.contents = self.contents + buf

sys.stderr.write("Testing %s\n" % pycurl.version)

start_time = time.time()

url = 'http://www.baidu.com/pycurl_test'
t = Test()
c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.perform()
end_time = time.time()
duration = end_time - start_time
print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL),c.getinfo(pycurl.NAMELOOKUP_TIME)
c.close()

print 'pycurl takes %s seconds to get %s ' % (duration, url)
print 'length of the content is %d ' % len(t.contents)
