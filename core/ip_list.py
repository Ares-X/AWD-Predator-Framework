# -*- coding: utf-8 -*-

# 生成ip列表
ipList = []


def ip_list(x):
    global ipList
    iplist = x.split('.')
    if '-' in x:
        for i in iplist:
            d = i
            if '-' in d:
                p = iplist.index(d)
                l = d.split('-')
                m = int(l[0])
                n = int(l[1])
        for j in range(m,n + 1):
            iplist[p] = str(j)
            ip = '.'.join(iplist)
            ipList.append(ip)
        ipList = sorted(set(ipList),key = ipList.index)  # 去重
    else:
        ip = '.'.join(iplist)
        ipList.append(ip)
        ipList = sorted(set(ipList),key = ipList.index)
    return ipList


def print_ip():
    global ipList
    for i in ipList:
        print i


def clear_ip():
    global ipList
    ipList = []


def remove_ip(ip):
    global ipList
    ipList.remove(ip)
