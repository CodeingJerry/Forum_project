from django.conf.urls import url
from article.views import article_list,create_article,ariticle_detail
from comment.views import create_comment

urlpatterns = [
    url(r'^lists/(?P<block_id>\d+)', article_list, name="article_list"),
    url(r'^create/(?P<block_id>\d+)', create_article, name="create_article"),
    url(r'^detail/(?P<article_id>\d+)', ariticle_detail, name="ariticle_detail"),
]