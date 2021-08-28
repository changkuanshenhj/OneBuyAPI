FROM duruo850/ubuntu18.04-python3.6:latest
MAINTAINER cxk 939083230@qq.com
WORKDIR /usr/src
RUN apt update
RUN apt install cron
RUN git clone git@github.com:changkuanshenhj/OneBuyAPI.git
WORKDIR /usr/src/OneBuyAPI
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver 0:80
