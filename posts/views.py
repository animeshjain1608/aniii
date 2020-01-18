from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from .models import Post
from .form import PostForm

# Create your views here.

def post_list(request):
    queryset_list = Post.objects.all() #.order_by("-timestamp")

    page_req_var = "page"
    paginator = Paginator(queryset_list, 2)
    page = request.GET.get(page_req_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset,
        "page_req_var" : page_req_var
    }
    return render(request, "list.html", context)

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,"Successfully created")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,"Not created")
    context = {
        "form" : form
    }
    return render(request, "post_form.html", context)

def post_details(request, id=None):
    context = {
        "obj" : get_object_or_404(Post, id=id)
    }
    return render(request, "post_detail.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=True)
            instance.save()
            messages.success(request,"Successfully updated")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,"Update failed")
    context = {
        "obj" : instance,
        "form" : form
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request,"Successfully deleted")
    return redirect("posts:list")