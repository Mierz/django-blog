from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Categorie

def index(request):
    latest_posts = Post.objects.all()
    paginator = Paginator(latest_posts, 1)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/index.html', {'latest_posts': posts})

def view(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'blog/view.html', context)