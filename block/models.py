#coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Block(models.Model):
      title = models.CharField(u"标题", max_length=30)
      des = models.CharField(u"描述", max_length=150)
      owner = models.ForeignKey(User,verbose_name="作者")

      create_timestamp = models.DateTimeField(auto_now_add=True)
      last_update_timestamp = models.DateTimeField(auto_now=True)

      def __unicode__(self):
            return self.title
      class Meta:
            verbose_name= u"板块"
            verbose_name_plural= u"板块"
