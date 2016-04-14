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
    pass
    # article = Article.objects.get(id=article_id)
