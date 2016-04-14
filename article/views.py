#coding: utf-8
# import sys
# import os
# add_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0,add_path)
# os.environ['DJANGO_SETTINGS_MODULE']='myforum.settings'
from django.shortcuts import render_to_response,redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
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
    (article_lists,pagination_data) = paginate_queryset(articles,page_no,cnt_per_page=1,half_show_length=5)
    return render_to_response("article_list.html",
                              {"articles":article_lists,
                               "b":block,
                               'has_previous':pagination_data['has_previous'],
                               'has_next':pagination_data['has_next'],
                               'previous_link':pagination_data['previous_link'],
                               'next_link':pagination_data['next_link'],
                               'page_cnt':pagination_data['page_cnt'],
                               'current_no':pagination_data['current_no'],
                               'page_links':pagination_data['page_links']},
                              context_instance=RequestContext(request))

    # p = Paginator(articles,1)
    # if page_no > p.num_pages:
    #     page_no = p.num_pages
    # if page_no <= 0:
    #     page_no = 1
    # page_links = [i for i in range(page_no - 5,page_no + 6) if i >0 and i <= p.num_pages]
    # page = p.page(page_no)
    # previous_link = page_links[0]-1
    # next_link = page_links[-1]+1
    # return render_to_response("article_list.html",
    #                           {"articles":page.object_list,"b":block,
    #                            'has_previous': previous_link >0,
    #                            'has_next':next_link <= p.num_pages,
    #                            'previous_link':previous_link,
    #                            'next_link':next_link,
    #                            'page_cnt':p.num_pages,
    #                            'current_no':page_no,
    #                            'page_links':page_links},
    #                           context_instance=RequestContext(request))

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
        owner = User.objects.all()[0]
        new_article = Article(block=block,owner=owner,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u'成功发布文章！')
        return redirect(reverse("article_list",args=[block.id]))

def ariticle_detail(request,article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    comment_page_no = int(request.GET.get('page_no','1'))
    comments = Comment.objects.filter(article=article)
    (comment_lists,pagination_data) = paginate_queryset(comments,comment_page_no,cnt_per_page=1,half_show_length=5)
    return render_to_response("article_detail.html",
                              {"comments":comment_lists,
                               'article':article,
                               'has_previous':pagination_data['has_previous'],
                               'has_next':pagination_data['has_next'],
                               'previous_link':pagination_data['previous_link'],
                               'next_link':pagination_data['next_link'],
                               'page_cnt':pagination_data['page_cnt'],
                               'current_no':pagination_data['current_no'],
                               'page_links':pagination_data['page_links']},
                              context_instance=RequestContext(request))
    # return render_to_response('article_detail.html',{'article':article},context_instance=RequestContext(request))
