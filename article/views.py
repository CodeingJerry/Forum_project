#coding: utf-8
# import sys
# import os
# add_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0,add_path)
# os.environ['DJANGO_SETTINGS_MODULE']='myforum.settings'
from django.shortcuts import render_to_response,redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from block.models import Block
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from models import Article
from comment.models import Comment
from utils.paginator import paginate_queryset

# Create your views here.
def article_list(request,block_id):
    block_id = int(block_id)
    page_no = int(request.GET.get('page_no','1'))
    block = Block.objects.get(id=block_id)
    articles = Article.objects.filter(block=block).order_by("-last_update_timestamp")
    (article_lists,pagination_data) = paginate_queryset(articles,page_no,cnt_per_page=2,half_show_length=5)
    return render_to_response("article_list.html",
                              {"articles":article_lists,
                               "b":block,
                               'pagination':pagination_data},
                              context_instance=RequestContext(request))

@login_required
def create_article(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == 'GET':
        return render_to_response('article_create.html',{'b':block},context_instance=RequestContext(request))
    else:
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,u'标题内容均不能为空')
            return render_to_response('article_create.html',{"b":block,"title":title,"content":content},context_instance=RequestContext(request))
        # owner = User.objects.all()[0]
        owner = request.user
        new_article = Article(block=block,owner=owner,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u'成功发布文章！')
        return redirect(reverse("article_list",args=[block.id]))

def ariticle_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    comment_page_no = int(request.GET.get('comment_page_no','1'))
    comments = Comment.objects.filter(article=article)
    (comment_lists,pagination_data) = paginate_queryset(comments,comment_page_no,cnt_per_page=2,half_show_length=5)
    return render_to_response("article_detail.html",
                              {"comments":comment_lists,
                               'article':article,
                               'pagination':pagination_data},
                              context_instance=RequestContext(request))
