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
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from OneBuyAPI import settings


def send_mail(request, email):
    print('send_email:', email)

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
]
