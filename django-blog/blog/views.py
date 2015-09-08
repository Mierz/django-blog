from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Categorie, Page

def index(request):
    latest_posts = Post.objects.all()
    paginator = Paginator(latest_posts, 10)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/index.html', {'latest_posts': posts})

def view(request, post_url):
    post = Post.objects.get(url=post_url)
    context = {'post': post}
    return render(request, 'blog/view.html', context)

def page(request, page_url):
    page = Page.objects.get(url=page_url)
    context = {'page': page}
    return render(request, 'blog/page.html', context)
    #return HttpResponse(page_link)

def category(request, category_id):
    return render(request, 'blog/category.html')