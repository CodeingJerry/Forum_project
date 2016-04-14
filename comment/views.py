from utils.response import json_response
from article.models import Article
from models import Comment
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from utils.paginator import paginate_queryset

# Create your views here.
@login_required()
def create_comment(request):
    article_id = int(request.POST['article_id'])
    to_comment_id = int(request.POST['to_comment_id'])
    content = request.POST['cotent'].strip()
    article = Article.objects.get(id=article_id)
    comment = Comment(block=article.block,article=article,owner=request.user,to_comment_id=to_comment_id,content=content)
    comment.save()
    return json_response({})

@login_required()
def comment_list(request):
    # article = Article.objects.get(id=article_id)
    comment_page_no = int(request.GET.get('page_no','1'))
    comments = Comment.objects.all()
    (comment_lists,pagination_data) = paginate_queryset(comments,comment_page_no,cnt_per_page=1,half_show_length=5)
    return render_to_response("article_detail.html",
                              {"comments":comment_lists,
                               # 'article':article,
                               'has_previous':pagination_data['has_previous'],
                               'has_next':pagination_data['has_next'],
                               'previous_link':pagination_data['previous_link'],
                               'next_link':pagination_data['next_link'],
                               'page_cnt':pagination_data['page_cnt'],
                               'current_no':pagination_data['current_no'],
                               'page_links':pagination_data['page_links']},
                              context_instance=RequestContext(request))