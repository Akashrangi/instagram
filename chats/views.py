from django.shortcuts import render
from chats.models import Chat
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def message_home(request):
    frd_name = request.GET.get('user', None)
    mychats_data = None
    if frd_name:
        if User.objects.filter(username = frd_name).exists() and Chat.objects.filter(user=request.user, frnd= User.objects.get(username= frd_name)).exists():
            frdn = User.objects.get(username=frd_name)
            mychats_data = Chat.objects.get(user=request.user,frnd=frdn).chats

    frnds = User.objects.exclude(pk=request.user.id)

    return render(request,'message.html',{'my':mychats_data,'chats': mychats_data,'frnds':frnds})
