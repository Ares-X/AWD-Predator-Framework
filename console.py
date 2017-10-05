#! -*- coding:utf-8 -*-

from cmd import Cmd
from core.flag import *
from core.shells import *
from core.ip_list import *

class MainConsole(Cmd):
    prompt = "apf> "
    Object = None
    def __init__(self):
        Cmd.__init__(self)

    # 打印装逼信息
    def preloop(self):
        string = """
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
getflag       get flag from targets with added webshell
submit        sutmit flag to server
exit          exit
showhelp      show core commands
help [x]      show command x's usage and description
                """
        print string
        print self.commandHelp


    def do_showhelp(self):
        print self.commandHelp

    def help_add(self):
        self.doc_header="this is the header"
        print "add : usage: add [shell path] [pwd] [type(eval/exec)] [method(get/post)]"
        print "      example: add :8001//a.php x eval get"

    def do_add(self,argv):
        array = argv.split(' ')
        if len(array)!=4:
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
        if array[2]=='eval':
            if array[3]=='get':
                GET_eval_shell_path_pwd(array[0],array[1])
                print "add ok"
                return
            if array[3]=='post':
                POST_eval_shell_path_pwd(array[0],array[1])
                print "add ok"
                return

        if array[2]=='exec':
            if array[3]=='get':
                GET_exec_shell_path_pwd(array[0],array[1])
                print "add ok"
                return
            if array[3]=='post':
                POST_exec_shell_path_pwd(array[0],array[1])
                print "add ok"
                return

    def help_load(self):
        print "load : usage : load"
        print "       load shell path and pwd"

    def do_load(self,argv):
        load_shell_path_pwd()

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
        array=argv.split('.')
        if len(array)<4:
            self.Error("the input was wrong")
            self.help_ip()
        ip_list(argv)

    def help_getflag(self):
        print "getflag  : usage : getflag curl xxxx "
        print "           example: getflag curl https:www.baidu.com"
        print "           if you have input this command and it works ,just run getflag!"

    def do_getflag(self,argv):
        global command
        if len(ipList)==0:
            self.Error("please set the ip list first!")
            self.help_ip()
            return
        if argv=='':
            if command=='':
                print "You should input full command at the first time , usage : getflag curl xxxx"
                return
            else:
                get_flag(ipList)
        else:
            set_command(argv)
            get_flag(ipList)

    def help_submit(self):
        print "submit : usage(the first time) : submit [url] [cookie](please remove ' ') [data](use '?' replace the flag )"
        print "         example: submit http:xxx.xxx.xx/xx/ JSESSIONID=A6F8;route=6cf03 pid=-1&pidName=&flag=?"
        print "         if you have input this command and it works ,just run submit!"


    def do_submit(self,argv):
        if len(flags)==0:
            self.Error("You don't have any flag,please get flag at first")
            self.help_getflag()
            return
        array=argv.split(' ')
        global url,datas,cookies
        if len(array)==0 and url != '' and cookies != '' and datas != '':
            submit_flag()
            return
        elif len(array)==0 and url =='' or cookies=='' or datas=='':
            self.Error("You should input full command at the first time : submit [url] [cookie] [data](use '?' replace the flag )")
            return
        elif len(array)!=0 and len(array)!=3:
            self.Error("input is wrong ! have you remove ' ' in cookie?")
            self.help_submit()
            return
        elif len(array)==3:
            if '?' not in array[2]:
                self.Error("please use ? replace the flag")
                return
            else:
                if array[0].startswith("http://") or array[0].notstartswith("https://"):
                    url = array[0],cookies = array[1],datas = array[2]
                    return
                else:
                    self.Error("url is not vaild!")
                    return



    def help_exit(self):
        print "exit "

    def do_exit(self,argv):
        print "Bye"
        #del self.object
        return True

    def help_showip(self):
        print "showip : usage: showip"
        print "         show ip list"

    def do_showip(self,argv):
        print_ip()

    def Error(self,info):
        print info
        return


if __name__=="__main__":
    a=MainConsole()
    a.cmdloop()