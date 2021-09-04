import uuid

from django.forms.widgets import TextInput, PasswordInput


class SendEmailButton(TextInput):
    # input_type = 'text'
    template_name = 'send_email_widget.html'

    # render_value 是否渲染现有的值
    def __init__(self, attrs=None, render_value=True):
        super().__init__(attrs)
        self.render_value = render_value

    def get_context(self, name, value, attrs):
        if not self.render_value:
            value = None
        return super().get_context(name, value, attrs)


class IDWidget(TextInput):

    def get_context(self, name, value, attrs):
        # 新增用户时:
        if not value:
            value = uuid.uuid4().hex

        return super().get_context(name, value, attrs)


class ImgWidget(TextInput):
    template_name = 'img1.html'


class PwdWidget(PasswordInput):
    def __init__(self, attrs=None, render_value=True):
        super().__init__(attrs)
        self.render_value = render_value
