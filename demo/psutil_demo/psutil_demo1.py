#!/usr/bin/env python
# encoding: utf-8

from __future__ import division
import psutil
import datetime

# 查看CPU 信息
print u"CPU 个数 %s" % psutil.cpu_count()
print u"物理CPU个数%s" % psutil.cpu_count(logical=False)
print u"CPU uptimes {}".format(psutil.cpu_times(percpu=False))
print "================================================"

# 查看内存信息
print psutil.virtual_memory()
print u"系统总内存 {} M".format(psutil.virtual_memory()[0]/1024/1024)
print u"系统可用内存 {} M".format(psutil.virtual_memory()[1]/1204/1024)
# print u"已使用内存占用 {} %".format((psutil.virtual_memory()[0]-psutil.virtual_memory()[1])/psutil.virtual_memory()[0] * 100)
print u"已使用内存占用 {} %.".format(psutil.virtual_memory()[2])
print u"已经用掉的内存大小 {} M.".format(psutil.virtual_memory()[3]/1024/1024)
print u"空闲未被分配的内存[Linux下不包括buffers和cached] {} M.".format(psutil.virtual_memory()[4]/1024/1024)
print u"最近使用内存和正在使用内存 {} M.".format(psutil.virtual_memory()[5]/1024/1024)
print u"已经分配但是没有使用的内存 {} M.".format(psutil.virtual_memory()[6]/1024/1024)
print u"一直存在内存中的部分，不会被移除 {} M.".format(psutil.virtual_memory()[7]/1024/1024)
print "================================================"

# 查看swap 信息
print psutil.swap_memory()
print u"swap的总大小 {} M.".format(psutil.swap_memory()[0]/1024/1024)
print u"已用swap大小 {} M.".format(psutil.swap_memory()[1]/1024/1024)
print u"空闲的swap大小 {} M.".format(psutil.swap_memory()[2]/1024/1024)
print u"已用swap的百分比 {} %.".format(psutil.swap_memory()[3])
print u"从磁盘调入到swap的大小 {} M.".format(psutil.swap_memory()[4]/1024/1024)
print u"从swap调出到磁盘的大小 {} M.".format(psutil.swap_memory()[5]/1024/1024)
print "================================================"

# 查看磁盘信息
print u"磁盘分区情况 {} .".format(psutil.disk_partitions())
disk_root = psutil.disk_usage('/')
print u"磁盘根目录总大小 {} G. 磁盘根目录使用大小 {} G. 磁盘根目录未使用大小 {} G. 磁盘根目录使用空间占用百分比 {} %.".format(disk_root[0]/1024/1024/1024,disk_root[1]/1024/1024/1024,disk_root[2]/1024/1024/1024,disk_root[3])
disk_io=psutil.disk_io_counters()
print "number of reads {}.".format(disk_io[0])
print "number of writes {}.".format(disk_io[1])
print "number of bytes read {} M.".format(disk_io[2]/1024/1024)
print "number of bytes written {} M.".format(disk_io[3]/1024/1024)
print "time spent reading from disk (in milliseconds) {}.".format(disk_io[4])
print "time spent writing to disk (in milliseconds) {}.".format(disk_io[5])
print "================================================"

# 查看网络信息
print psutil.net_connections()
# 返回系统的整个socket连接的信息，可以选择查看哪些类型的连接信息，类似于netstat命令

# net_io = psutil.net_io_counters(pernic=True) # pernic=True 显示各个网卡的信息
net_io = psutil.net_io_counters()
print u"发送的字节数 {} M.".format(net_io[0]/1024/1024)
print u"接收的字节数 {} M.".format(net_io[1]/1024/1024)
print u"发送的数据包个数 {}.".format(net_io[2])
print u"接收的数据包个数 {}.".format(net_io[3])
print u"接收的数据包错误的总数 {}.".format(net_io[4])
print u"发送的数据包错误的总数 {}.".format(net_io[5])
print u"接收时丢弃的数据包的总数 {}.".format(net_io[6])
print u"发送时丢弃的数据包的总数[OSX和BSD系统总数0] {}.".format(net_io[7])
print "================================================"

# 当前登录系统的用户信息
print psutil.users()
print "================================================"

# 获取系统开机时间
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
print "================================================"

# 进程信息
print u"列出所有进程pid {}.".format(psutil.pids())
p = psutil.Process(7359)
print u"进程名：{} .".format(p.name())
print u"进程bin路径: {} .".format(p.exe())
print u"进程工作的绝对路径: {} .".format(p.cwd())
print u"进程状态: {} .".format(p.status())
print u"进程创建时间: {} .".format(datetime.datetime.fromtimestamp(p.create_time()).strftime('%Y-%m-%d %H:%M:%S'))
print u"进程uid信息: {} .".format(p.uids())
print u"进程gid信息: {} .".format(p.gids())
print u"进程cpu时间: {} .".format(p.cpu_times())
print u"进程cpu亲和度: {} .".format(p.cpu_affinity())
print u"进程内存利用率: {} .".format(p.memory_percent())
print u"进程内存rss/vms信息: {} .".format(p.memory_info())
print u"进程io信息: {} .".format(p.io_counters())
print u"返回打开进程socket的namedutples列表: {} .".format(p.connections())
print u"进程开启的线程数: {} .".format(p.num_threads())

print "================================================"
