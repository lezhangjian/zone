from django.db import models

# Create your models here.


class LiuyanModels(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"姓名")
    message = models.CharField(max_length=600, verbose_name=u"留言")
    add_time = models.DateTimeField(auto_now=True, verbose_name=u"添加时间")