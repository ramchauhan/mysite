from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
#from django.core.context_processors import cs
from django.core.context_processors import csrf
from django.views.generic import ListView


from core.models import Post, Comment, BannerImages, ClassStandard, AllQuestion
from mysite.settings import MEDIA_URL
from core.forms import CommentForm
from django.template import RequestContext

import time
from calendar import month_name
from django.http.response import HttpResponseRedirect


def main(request): 
    posts     = Post.objects.all().order_by("created")
    paginator = Paginator(posts, 2)
    
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages) 
        
    return render_to_response("blog/list.html", dict(posts=posts, user=request.user), context_instance=RequestContext(request))


def post(request, pk):
    post    = Post.objects.get(pk=int(pk))
    comment = Comment.objects.filter(post=post)
    dis   = dict(post=post, comment=comment, form=CommentForm(), user=request.user)
    dis.update(csrf(request))
    return render_to_response("blog/post.html", dis)


def delete_comment(request, post_pk, pk=None):
    """Delete comment(s) with primary key `pk` or with pks in POST."""
    if request.user.is_staff:
        if not pk: pklst = request.POST.getlist("delete")
        else: pklst = [pk]

        for pk in pklst:
            Comment.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse("core.views.post", args=[post_pk]))

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("core.views.post", args=[pk]))




def mkmonth_lst():
    """Make a list of months to show archive links."""

    if not Post.objects.count(): return []

    # set up vars
    year, month = time.localtime()[:2]
    first = Post.objects.order_by("created")[0]
    fyear = first.created.year
    fmonth = first.created.month
    months = []

    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    return months

def month(request, year, month):
    """Monthly archive."""
    posts = Post.objects.filter(created__year=year, created__month=month)
    return render_to_response("blog/list.html", dict(post_list=posts, user=request.user,
                                                months=mkmonth_lst(), archive=True))



## Here is the code by classbased views

class HomePageView(ListView):
    model = BannerImages
    template_name = "core/homepage/homepage.html"

    def get_context_data(self, **kwargs):
	context = super(HomePageView, self).get_context_data(**kwargs)
        context['class_data'] = ClassStandard.objects.all()
        context['all_question'] = AllQuestion.objects.all()
	context['media_url'] = MEDIA_URL
	return context


class AllQuestionView(ListView):
    model = AllQuestion
    template_name = "core/allquestions.html"
    context_object_name = "question"
   
    def get_context_data(self, **kwargs):
	context = super(AllQuestionView, self).get_context_data(**kwargs)
	context['media_url'] = MEDIA_URL
	return context

	 
