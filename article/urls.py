from django.conf.urls import url
from article.views import article_list

urlpatterns = [
    url(r'^lists/(?P<block_id>\d+)', article_list, name="article_list"),
]