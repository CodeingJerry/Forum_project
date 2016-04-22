from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Block
from message.models import UserMessage
from usercenter.views import UserProfile

# Create your views here.
def block_list(request):
    if request.user.is_authenticated():
        msg_cnt=UserMessage.objects.filter(status=0,owner=request.user).count()
        profile=UserProfile.objects.get(owner=request.user)
    else:
        msg_cnt=0
        profile=None
    blocks=Block.objects.all().order_by("-id")
    return render_to_response("block_list.html", {"blocks": blocks,'msg_cnt':msg_cnt,'profile':profile},context_instance=RequestContext(request))
