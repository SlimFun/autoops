#!/usr/bin/env python
# encoding: utf-8

from IPy import IP
from IPy import IPSet

ip1 = IP('192.168.0.0/30')
ip2 = IP('192.168.0.2/24',make_net=True)
ip3 = IP('127.0.0.1')
ip4 = IP('::1')

for i in ip1:
    print u'192.168.0.0/30 IP 地址: {}.'.format(i)

print u'192.168.0.0/30 网络IP地址数量: {}.'.format(ip1.len())
print u'192.168.0.0/24 网络IP地址数量: {}.'.format(ip2.len())

print u'192.168.0.0/30 ip地址反向解析列表: {}.'.format(ip1.reverseNames())
print ip1.reverseName()

print u'192.168.0.0/30 IP地址类型: {}.'.format(ip1.iptype())
print u'127.0.0.1 IP 地址类型: {}.'.format(ip3.iptype())

print u'127.0.0.1 为: IPv{}.'.format(ip3.version())
print u'::1 为: IPv{}.'.format(ip4.version())

print IP('10')
print IP(0x7f000001)

print IP('127.0.0.0/8')
print IP('127.0.0.0/255.0.0.0')
print IP('127.0.0.0-127.255.255.255')
print IP('127.0.0.1/255.0.0.0',make_net=True)
print IP('127.0.0.1').make_net('255.0.0.0')

print '============================================='

print u'IP地址转字符串的几种方式:'
ip5 = IP('10.0.0.0/32')
ip6 = IP('10.0.0.0/24')
ip7 = IP('10.0.0.0')
print ip5.strNormal()
print ip6.strNormal()
print ip6.strNormal(0)
print ip6.strNormal(1)
print ip6.strNormal(2)
print ip6.strNormal(3)
print ip7
ip7.NoPrefixForSingleIp = None
print(ip7)
ip7.WantPrefixLen = 3
print ip7

print '============================================='

print IP('10.0.0.0/22') - IP('10.0.2.0/24')
print IPSet([IP('10.0.0.0/23'), IP('10.0.3.0/24'), IP('10.0.2.0/24')])

s = IPSet([IP('10.0.0.0/22')])
s.add(IP('192.168.1.2'))
print s
s.discard(IP('192.168.1.2'))
print s
