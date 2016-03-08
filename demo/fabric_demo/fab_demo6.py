#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run,env,roles,execute

'''
fabric test.
'''

env.hosts = ['192.168.99.101','192.168.99.102'] # 本测试中env.hosts可以不设置，会使用env.passwords里面的主机地址
# env.exclude_host = ['192.168.99.101']
env.user = 'root'
env.port = 22
env.passwords = {
    'root@192.168.99.101:22': 'python',
    'root@192.168.99.102:22': 'linux',
}
env.roledefs = {
    'testserver1': ['192.168.99.101'],
    'testserver2': ['192.168.99.102']
}

@roles('testserver1')
def test1():
    run('echo "test server 1."')

@roles('testserver2')
def test2():
    run('echo "test server 2."')

@roles('testserver1','testserver2')
def testall():
    run('echo "test servers all."')

def test():
    execute(test1)
    execute(testall)
    execute(test2)
