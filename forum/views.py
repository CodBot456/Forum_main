from django.shortcuts import render
from django.http import HttpResponseRedirect
from forum.models import Forum, Comment
from django.urls import reverse

# Create your views here.
def home_view(request):
    return render(request,"forum/home.html")

def forums_view(request):
    context = {
        "forums": Forum.objects.all()
    }
    return render(request,"forum/forums.html", context)

def forum_detail_view(request, forum_id):
    if request.method=='POST':
        comment = request.POST.get('comment')
        Comment.objects.create(author=request.user, body = comment, forum = Forum.objects.get(id=forum_id))
        return HttpResponseRedirect(reverse('forum', args=(forum_id,)))
    
    filter = request.GET.get('filter')
    context = {
        "forum": Forum.objects.get(id=forum_id)
    }
    if filter == 'timefromold':
        context["sorted_comments"] = Forum.objects.get(id=forum_id).comment_set.order_by('published')
    elif filter == 'timefromnew':
        context["sorted_comments"] = Forum.objects.get(id=forum_id).comment_set.order_by('-published')
    else:
        context["sorted_comments"] = Forum.objects.get(id=forum_id).comment_set.order_by('published')
    return render(request,"forum/forum_detail.html", context)


def delete_comment(request, forum_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return HttpResponseRedirect(f"http://127.0.0.1:8000/forum-detail/{forum_id}/")