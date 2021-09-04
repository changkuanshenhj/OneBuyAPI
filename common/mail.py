from django.core.mail import send_mail as dj_send_mail


def send_mail(title, message, receivers):
    print('---------开始发送邮件------')
    dj_send_mail(title, '', html_message=message,
                 from_email='cxk_370456@163.com',
                 recipient_list=receivers)
    print('-----发送完成-----')
