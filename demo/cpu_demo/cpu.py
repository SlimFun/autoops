#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import simplejson as json


class CpuData(object):
    def __init__(self):
        self.now_data = {}
        self.last_data = {}

    def get_now_data(self):
        # 获取当前数据
        try:
            raw_data = file('/proc/stat').readlines()
        except:
            return (-1, 'system file not exist', '')

        results = raw_data[0].strip()
        cpu_all = results.split()
        cpu_all.pop(0)
        cpu_data = [int(i) for i in cpu_all]
        self.now_data['idle'] = cpu_data[3]
        self.now_data['total'] = sum(cpu_data)
        return (0, '', self.now_data)

    def get_last_data(self):
        # 获取历史数据
        try:
            raw_data = file('/tmp/proc_stat').read()
            self.last_data = json.loads("%s" % raw_data.strip())
        except:
            self.last_data = self.now_data

        # 保存当前数据到历史数据表中
        fp = file('/tmp/proc_stat', 'w')
        fp.write(json.dumps(self.now_data))
        fp.close()
        return (0, '', self.last_data)

    def compute_data(self):
        now_status, now_msgs, now_data = self.get_now_data()
        last_status, last_msgs, last_data = self.get_last_data()
        if now_status == last_status == 0:
            # 处理两个数据，得到要计算的值
            results = {}
            diff_total = int(now_data['total']) - int(last_data['total'])
            diff_idle = (int(now_data['idle']) - int(last_data['idle']))
            if diff_total > 0:
                real_data = 100 * (float(diff_total - diff_idle) / diff_total)
                results['cpuuse'] = int(round(real_data))
            else:
                # 第一次加载的时候，历史数据为空，无法计算， 所有初始化为0
                results['cpuuse'] = 0
            return (0, '', results)
        elif now_status != 0:
            return (now_status, now_msgs, now_data)
        else:
            return (last_status, last_msgs, last_data)

    def run(self):
        while True:
            result = self.compute_data()
            if result[0] == 0:
                print result
            else:
                print result
                break
            time.sleep(1)

if __name__ == "__main__":
    cpudata = CpuData()
    cpudata.run()
