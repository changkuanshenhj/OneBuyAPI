import re
from django import forms
from .models import AppUser
from django.core.exceptions import ValidationError
from .widgets import SendEmailButton, IDWidget, ImgWidget, PwdWidget


class UserForm(forms.ModelForm):
    id = forms.CharField(widget=IDWidget, label='主键', disabled=True)

    name = forms.CharField(min_length=8,
                           max_length=20,
                           required=True,
                           error_messages={
                               'required': '账户不能为空',
                               'max_length': '账户不能超出20个字符',
                               'mix_length': '账户不能少于8个字符'
                           })
    phone = forms.CharField(max_length=11,
                            min_length=11,
                            required=True,
                            label='手机号')

    # 通过widget属性指定自定义widget部件
    email = forms.CharField(required=True,
                            label='邮箱',
                            widget=SendEmailButton)

    auth_key = forms.CharField(widget=PwdWidget,
                               # 一样的效果widget=forms.PasswordInput(render_value=True),
                               label='口令',
                               min_length=6,
                               error_messages={
                                   'required': '口令不能为空',
                                   'min_length': '口令不少于6位'
                               })

    img1 = forms.CharField(max_length=100,
                           widget=ImgWidget,
                           required=False)

    def clean_auth_key(self):
        # 以上验证都通过了
        # 自定义验证规则：必须包含大写、小写和数字等字符
        auth_key = self.cleaned_data.get('auth_key')
        if all((
                re.search(r'\d+', auth_key),
                re.search(r'[a-z]+', auth_key),
                re.search(r'[A-Z]+', auth_key)
        )):
            print('---clean_auth_key----')
            return auth_key

        raise ValidationError('口令必须包含大写、小写和数字等字符')

    # 出大问题出处。（查看其原理）
    # def is_valid(self):
    #     print('--is_vaild()--')
    #     return super().is_valid()

    class Meta:
        model = AppUser
        fields = ['id', 'img1', 'name', 'auth_key', 'phone', 'email']
        error_messages = {

        }

