import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class YGBaseModel(models.Model):
    id = models.CharField(max_length=50,
                          primary_key=True,
                          verbose_name='ID')

    class Meta:
        abstract = True  # 声明为抽象模型


@receiver(pre_save)
def new_uuid_value(sender, **kwargs):
    if issubclass(sender, YGBaseModel):
        instance = kwargs.get('instance')
        if instance.id is None:
            instance.id = uuid.uuid4().hex
            # instance.id = str(uuid.uuid4()) 带横杠的uuid码
