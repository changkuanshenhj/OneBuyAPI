# 一、Docker的基本用法与快速部署项目

## 1.1 基本说明

主流的开发模式：DevOps开发即运维

Docker是基于容器技术（虚拟技术），包含Docker仓库、镜像、容器。Docker.io安装完成后，默认存在两个进程即Client和Server（守护进程 damon）。一个镜像可以运行多次，每次都会产生容器子进程。

```
apt install docker.io
```

```
sudo systemctl start docker
sudo systemctl enable docker
```



## 1.2 Docker常用的命令

+ docker version
+ docker search 镜像名
+ docker pull 镜像全名称
+ docker images 查看所有的本地镜像

```
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
redis        latest    ddcca4b8a6f0   8 days ago   105MB
```

+ docker run   启动镜像

同步运行镜像

```
docker run --name redis1 redis  # ctrl + c 退出
```

 后台运行，且映射端口

```
docker run -dit --name redis1 -p 6377:6379 redis
```

查看所有容器进程

```
docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED        STATUS          PORTS 
aeb74284e635   redis     "docker-entrypoint.s…"   13 hours ago   Up 11 seconds   0.0.0.0:6377->6379/tcp, :::6377->6379/tcp   NAMES:redis1

```

停止容器进程

```
docker stop redis1
```

启动容器进程

```
docekr start redis1
```

删除容器（-f   强制删除）

```
docker rm -f redis1
```

删除镜像

```
docker rmi 镜像名或镜像ID
```

python测试连接的代码

```python
from redis import Redis
from sys import argv

config = { 
        'host': '192.168.31.161',
        'port': argv[1],
        'db': 2
        }
client = Redis(**config)
print('Redis success %s' % str(config))
```

运行脚本：（git base环境下）

```
python test_conn.py 6377
```

进入容器

```
# 只执行如redis1容器的命令，查看当前容器的工作目录下的文件
docker exec 容器名 ls

# 使用-it 进入容器的内部
docker exec -it 容器名 /bin/sh
```

```
# pip freeze > requirements.txt
```

http://192.168.1.103/admin/

## 1.3 Dockerfile的用法

+ 文件内容

```dockerfile
FROM duruo850/ubuntu18.04-python3.6:latest
MAINTAINER cxk 939083230@qq.com
WORKDIR /usr/src
RUN apt update
RUN apt install cron
RUN apt-get install git -y
RUN git clone http://github.com/changkuanshenhj/OneBuyAPI.git
WORKDIR /usr/src/OneBuyAPI
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver 0:80
```

RUN命令：执行容器的linux命令

CMD命令：镜像运行时时执行的命令

WORKDIR命令：在容器中，切换到某一工作目录，之后的命令中文件路径是相对于当前工作目录

【注意】

①有些Ubuntu中并不自带git，所有在自定义镜像的时候，需要在命令里面安装不存在的软件。

如：apt update；apt-get install git -y；apt install cron。

②容器最后执行的命令使用CMD

③chmod +x auto_down.sh脚本变成可执行的文件。

+ 定时拉取更新工程：（每隔一分钟）

auto_down.cron（一定要多一行空的，即光标在第二行保存文件）

```cron
*/1 * * * *  /usr/src/OneBuyAPI/auto_down.sh

```

+ auto_down.sh

```sh
#!/bin/sh
cd /usr/src/OneBuyAPI/
git pull
```

【注意】：第一行表示谁去执行当前的脚本，即脚本执行对象。

+ 编译Dockerfile文件

```
docker build -t onebuy:1.0 .
```

  ①" . "表示在当前的目录下进行构建镜像onebuy表示镜像名。②":1.0"表示版本号。

+ 运行自己的镜像----->容器

```
docker run -itd --name web_server -p 80:80 镜像ID
```

+ 导入导出镜像

```
docker save -o ~/onebuy.tar 镜像名/ID
# ~/project.tar表示保存到什么位置,"~"是最初始的地方
# cd ~  尝试
```

```
docker load < ~/onebuy.tar
docker load --input ~/onebuy.tar
以上两者一样的效果，表示导入镜像

docker tag onebuy:latest 镜像ID # 为镜像起名字 
```

+ 别的服务器想下载当前的镜像

```
mkdir imgs
cd imgs
scp root@192.168.1.103:~/onebuy.tar .
```

## 1.4 Ubuntu系统中的一些命令

①：sudo apt-get install openssh-server ; ssh-keyen -A  （经过这两步，可以远程ssh连接Ubuntu服务器）

②：（git base下）远程连接命令：ssh cxk@192.168.1.103  cxk表示的是Ubuntu中的用户名，使用root是连接不了的，只能连接后进入再切换用户：su root 

③：ip a 查看外界可连的ip地址（192.168.1.103 ）

④：远程退出当前用户使用：exit/logout (退出时，必须退回不在任何目录下才可以)。

⑤：关机：shutdown -h now

⑥：更新：apt update  

⑦：安装软件：apt-get install git -y

https://github.com/FriendShip-Team/OneGuyAPI/

https://github.com/XA1903LastTeam/OneGouAPI
