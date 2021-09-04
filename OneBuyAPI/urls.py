"""OneBuyAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail as send_163_email

from threading import Thread

from common.mail import send_mail as my_send_mail

from OneBuyAPI import settings


def send_mail(request, email):
    print('send_email:', email)

    subtitle = '用户激活通知'
    message = '<html>亲爱的，注册用户ck！请<a href="/">激活</html>'

    # send_163_email(subject=subtitle, message='', html_message=message,
    #                from_email='cxk_370456@163.com',
    #                recipient_list=[email, ])

    # Thread(target=send_163_email,
    #        kwargs={
    #            'subject': subtitle,
    #            'message': '',
    #            'html_message': message,
    #            'from_email': 'cxk_370456@163.com',
    #            'recipient_list': [email, ]
    #        }).start()

    # 使用线程去调用自定义保装函数去发送邮件
    Thread(target=my_send_mail,
           kwargs={
               'title': subtitle,
               'message': message,
               'receivers': [email]
           }).start()

    return JsonResponse({
        'msg': '发送成功',
        'info': {
            'email': email
        }
    })


@csrf_exempt
def upload_img(request, user_id):
    # post请求

    # user_id 作为头像的文件名

    img1File: InMemoryUploadedFile = request.FILES.get('img')
    img_name = user_id + '.' + img1File.name.split('.')[-1]
    filepath = os.path.join(settings.MEDIA_ROOT, img_name)
    with open(filepath, 'wb') as f:
        for img in img1File.chunks():  # 分包写入
            f.write(img)
    print('图片本地保存成功')
    return JsonResponse({
        'code': 200,
        'msg': '上传成功',
        'path': '/media/' + img_name
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_mail/<email>/', send_mail),
    path('upload_img/<user_id>/', upload_img),
    path('user1/', include('user1.urls')),
]
