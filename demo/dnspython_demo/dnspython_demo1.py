#!/usr/bin/env python
# encoding: utf-8

from dns import resolver
from dns import name

domain_a = raw_input('Pls input domain resolve to A:')
a = resolver.query(domain_a,'A')
for i in a.response.answer:
    for j in i.items:
        print j.address

domain_mx = raw_input('Pls input domain resolve to MX:')
mx = resolver.query(domain_mx,'MX')
for i in mx:
    print 'mx preference:',i.preference,' mail exchanger=',i.exchange

domain_ns = raw_input('Pls input domain resolve to NS:')
ns = resolver.query(domain_ns,'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()

domain_cname = raw_input('Pls input domain resolve to CNAME:')
cname = resolver.query(domain_cname,'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()

n = name.from_text('www.xingshulin.com')
o = name.from_text('xingshulin.com')
print n.is_subdomain(o)
print n.is_superdomain(o)
print n > o
rel = n.relativize(o)
n2 = rel + o
print n2 == n
print n.labels
