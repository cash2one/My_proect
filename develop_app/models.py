# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Idc(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'名称')
    address = models.CharField(max_length=128,verbose_name=u'地址')
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'机房'
        verbose_name_plural = verbose_name

# 主机组类
class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组信息'
        verbose_name_plural = verbose_name

class Server(models.Model):
    hostname = models.CharField(max_length=128,verbose_name=u'主机名')
    ip = models.GenericIPAddressField(max_length=128,verbose_name=u'IP地址')
    group = models.ManyToManyField(Group, null=True, blank=True, verbose_name=u'组名')
    idc = models.CharField(max_length=40,verbose_name=u'所属机房')
    cabinet = models.CharField(max_length=32,verbose_name=u'机柜位置')
    remark = models.CharField(max_length=128,verbose_name=u'备注')

    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = u'服务器列表'
        verbose_name_plural = verbose_name

class Host(models.Model):
    hostname = models.CharField(max_length=32, verbose_name=u'主机名')
    ip = models.CharField(max_length=32, verbose_name=u'IP地址')
    os = models.CharField(max_length=32,verbose_name=u'操作系统')
    mem = models.CharField(max_length=128,verbose_name=u'内存')
    disk = models.CharField(max_length=256,verbose_name=u'磁盘')
    physical_cpu = models.PositiveSmallIntegerField(verbose_name=u'CPU物理核数')
    logical_cpu = models.PositiveSmallIntegerField(verbose_name=u'CPU逻辑核数')
    serialnumber = models.CharField(max_length=80,unique=True,verbose_name=u'序列号')

    def __unicode__(self):
        return self.hostname

    class Meta:
        verbose_name = u'主机信息'
        verbose_name_plural = verbose_name


