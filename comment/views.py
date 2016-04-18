# coding: utf-8
from utils.response import json_response
from article.models import Article
from models import Comment
from message.models import UserMessage
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from utils.paginator import paginate_queryset
from article.views import ariticle_detail

# Create your views here.
@login_required()
def create_comment(request):
    article_id = int(request.POST['article_id'])
    current_href = request.POST['current_href'].strip()
    to_comment_id = int(request.POST['to_comment_id'])
    content = request.POST['content'].strip()
    article = Article.objects.get(id=article_id)
    comment = Comment(block=article.block,article=article,owner=request.user,to_comment_id=to_comment_id,content=content)
    comment.save()
    if to_comment_id == 0:
        new_msg = UserMessage(owner=article.owner,
            content=u'有人评论了您的文章(%s)' % article.title,
            link=reverse('ariticle_detail',args=[article.id]))
        new_msg.save()
    else:
        to_comment = Comment.objects.get(id=to_comment_id)
        new_msg = UserMessage(owner=to_comment.owner,
            content=u'有人评论了您的评论(%s)' % to_comment.content[:30],
            # link=reverse('ariticle_detail',args=[article.id]))
            # link=reverse('ariticle_detail',
            #              kwargs={'article.id':article.id,'comment_page_no':ariticle_detail(article_id).pagination_data.page_no}))
            # link=reverse('ariticle_detail',args=[article.id])+'?comment_page_no='+ current_href
            link=current_href)
        new_msg.save()
    return json_response({})

@login_required()
def comment_list(request):
    pass

