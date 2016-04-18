# coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserMessage(models.Model):
      content = models.CharField(u"内容", max_length=400)
      owner = models.ForeignKey(User,verbose_name=u"作者")
      link = models.CharField(u'链接',max_length=400,default='block_list.html')
      status = models.IntegerField(u"状态",choices=((0,u"未读"),(1,u"已读")),default=0)

      create_timestamp = models.DateTimeField(auto_now_add=True)
      last_update_timestamp = models.DateTimeField(auto_now=True)

      def __unicode__(self):
          return self.content

      class Meta:
            verbose_name= u"用户评论"
            verbose_name_plural= u"用户评论"
