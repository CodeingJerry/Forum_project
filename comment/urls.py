#coding: utf-8
from django.conf.urls import url
from views import create_comment,comment_list
from article.views import ariticle_detail

urlpatterns = [
    url(r'^lists/$', comment_list, name="comment_list"),
    url(r'^create/$', create_comment, name="create_comment"),

]