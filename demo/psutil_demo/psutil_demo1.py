#!/usr/bin/env python
# encoding: utf-8

import psutil
import datetime

# display cpu info
print u"CPU 个数 %s" % psutil.cpu_count()
print u"物理CPU个数%s" % psutil.cpu_count(logical=False)
print u"CPU uptimes"
print psutil.cpu_times()
